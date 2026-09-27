from collections import Counter
from collections import defaultdict

# data-dump um dict com a lista dos cientitas de dados

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

friendship_pairs = [
    (0, 1),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (6, 8),
    (7, 8),
    (8, 9),
]

interests = [
    (0, "Hadoop"),
    (0, "Big Data"),
    (0, "HBase"),
    (0, "Java"),
    (0, "Spark"),
    (0, "Storm"),
    (0, "Cassandra"),
    (1, "NoSQL"),
    (1, "MongoDB"),
    (1, "Cassandra"),
    (1, "HBase"),
    (1, "Postgres"),
    (2, "Python"),
    (2, "scikit-learn"),
    (2, "scipy"),
    (2, "numpy"),
    (2, "statsmodels"),
    (2, "pandas"),
    (3, "R"),
    (3, "Python"),
    (3, "statistics"),
    (3, "regression"),
    (3, "probability"),
    (4, "machine learning"),
    (4, "regression"),
    (4, "decision trees"),
    (4, "libsvm"),
    (5, "Python"),
    (5, "R"),
    (5, "Java"),
    (5, "C++"),
    (5, "Haskell"),
    (5, "programming languages"),
    (6, "statistics"),
    (6, "probability"),
    (6, "mathematics"),
    (6, "theory"),
    (7, "machine learning"),
    (7, "scikit-learn"),
    (7, "Mahout"),
    (7, "neural networks"),
    (8, "neural networks"),
    (8, "deep learning"),
    (8, "Big Data"),
    (8, "artificial intelligence"),
    (9, "Hadoop"),
    (9, "Java"),
    (9, "MapReduce"),
    (9, "Big Data"),
]

salaries_and_tenures = [
    (8300, 8.7),
    (88000, 8.1),
    (48000, 0.7),
    (76000, 6),
    (69000, 6.5),
    (76000, 7.5),
    (60000, 2.5),
    (83000, 10),
    (48000, 1.9),
    (63000, 4.2),
]

# inicialize o dict com uma lista vazia para cada id de usuário:
friendship = {user["id"]: [] for user in users}

# Loop pelos pares de amigos para preenchê-la:
for i, j in friendship_pairs:
    friendship[i].append(j)  # Adiciona j como amigo de usuário i
    friendship[j].append(i)  # Adiciona i como amigo do usuário j


def number_of_friends(user):
    """Quantos amigos tem o _user_?"""
    user_id = user["id"]
    friend_ids = friendship[user_id]
    return len(friend_ids)


total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connections / num_users

# Cria uma lista de (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

# Classifique a lista por num_friends do maior para o menor
num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)


# Iterar amigos dos amigos
def foaf_ids_bad(user):
    """foaf significa friend of a friend [amigo de um amigo]"""
    return [
        foaf_id
        for friend_id in friendship[user["id"]]
        for foaf_id in friendship[friend_id]
    ]


# Contagem de amigos em comum porém excluindo as pessoas que o usuário ja conhece
def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendship[user_id]  # Para cadd amigo meu,
        for foaf_id in friendship[friend_id]  # encontre os amigos deles
        if foaf_id != user_id  # que não sejam eu
        and foaf_id not in friendship[user_id]  # e não sejam meus amigos.
    )


print(friends_of_friends(users[3]))


# Encontrar usuários com o mesmo interesse
def data_scientists_who_like(target_interest):
    """Encontra os ids dos usuários com o mesmo interesse"""
    return [
        user_id
        for user_id, user_interest in interests
        if user_interest == target_interest
    ]


# As cahves são interesses, os valores são listas de user_ids com interesse em questão
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# As chaves são user_ids, os valores são listas de interesse do user_id em questão.
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)


def most_common_interests_with(user):
    return Counter(
        interest_user_id
        for interest in interests_by_user_id[user["id"]]
        for interest_user_id in user_ids_by_interest[interest]
        if interest_user_id != user["id"]
    )


# As chaves são anos, os valores são listas de salários por anos de experiência.
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# As chaves são anos, cada valor é o salário médio associado ao número de anos de experiência.
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}


# Buckets de experiência
def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"


# As chaves são Buckets de anos de experiência, os valores são as listas de salários associados ao Bucket em questão.
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# Computação média salarial de cada grupo.
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}


# Quantos usuários pagam por suas contas e quantos não pagam.
def predic_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"


# Tópicos de interesse
words_and_counts = Counter(
    word for user, interest in interests for word in interest.lower().split()
)

# Facilita a listagem de palavras que ocorrem mais de uma vez.
for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)
