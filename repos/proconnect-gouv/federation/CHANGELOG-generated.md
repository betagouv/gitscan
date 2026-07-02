## Changelog : federation (30 derniers jours, au 30 juin 2026)

### Résumé
Ce mois-ci, les évolutions de la plateforme se concentrent sur l'amélioration de la gestion des collaborateurs, la correction de bugs et la mise à jour des dépendances pour assurer la sécurité et la stabilité du système. Des améliorations ont également été apportées à l'interface d'administration et à l'intégration avec des services tiers comme Bitwarden.

### Évolutions fonctionnelles
- Ajout de la gestion des collaborateurs pour les clients OIDC [#1312](https://github.com/proconnect-gouv/federation/issues/1312).
- Possibilité de rechercher des utilisateurs fédérés par adresse email dans l'interface d'administration [#1307](https://github.com/proconnect-gouv/federation/issues/1307).
- Ajout de la possibilité de bloquer des utilisateurs dans l'interface d'administration [#1254](https://github.com/proconnect-gouv/federation/issues/1254).
- Amélioration de l'autocomplétion Bitwarden pour le champ mot de passe [#1309](https://github.com/proconnect-gouv/federation/issues/1309).
- Mise à jour de la classification des services publics pour correspondre à la définition légale actuelle [#1215](https://github.com/proconnect-gouv/federation/issues/1215).
- Ajout de la gestion des collaborateurs pour les utilisateurs partenaires [#1310](https://github.com/proconnect-gouv/federation/issues/1310).

### Évolutions techniques
- Abaissement de la version de PostgreSQL à 16 pour alignement avec la production [#1311](https://github.com/proconnect-gouv/federation/issues/1311).
- Suppression de la configuration SSL MongoDB restante [#1323](https://github.com/proconnect-gouv/federation/issues/1323).
- Suppression de PM2 des images de production pour simplifier le déploiement [#1244](https://github.com/proconnect-gouv/federation/issues/1244).
- Ajout du support Sentinel pour Redis [#1265](https://github.com/proconnect-gouv/federation/issues/1265).
- Configuration de la connexion MongoDB TLS via variable d'environnement [#1266](https://github.com/proconnect-gouv/federation/issues/1266).
- Amélioration de la gestion des healthchecks avec l'ajout de `readyz` [#1261](https://github.com/proconnect-gouv/federation/issues/1261).
- Refactorisation du service OIDC provider [#1288](https://github.com/proconnect-gouv/federation/issues/1288).
- Suppression des certificats TLS orphelins dans les volumes Docker [#1286](https://github.com/proconnect-gouv/federation/issues/1286).
- Mise à jour des dépendances vers les dernières versions stables (voir section "Autres changements").

### Autres changements
- Mise à jour des dépendances : plusieurs dépendances ont été mises à jour vers leurs dernières versions pour améliorer la sécurité et la stabilité du projet. Ces mises à jour incluent des paquets comme `mongodb`, `pg`, `uuid`, `fastapi`, `amqplib`, `ejs`, `moment-timezone`, `nginx`, `cryptography`, `pytest`, `ruff`, `jest`, `cypress`, `prettier`, `ts-jest`, `ts-loader`, `form-data`, `axe-core`, `js-yaml`, `otplib`, `commander`, `ts-loader`, `uvicorn`, `jose`, `ioredis` et d'autres.
- Suppression des règles d'ignorance pour les mises à jour de PostgreSQL [#1294](https://github.com/proconnect-gouv/federation/issues/1294).
- Suppression des configurations TLS locales pour MongoDB et Redis [#1283](https://github.com/proconnect-gouv/federation/issues/1283), [#1285](https://github.com/proconnect-gouv/federation/issues/1285).
- Mise à jour du label du checkbox "Se souvenir de moi" [#1301](https://github.com/proconnect-gouv/federation/issues/1301).
- Correction d'un bug lié à la gestion des domaines sans enregistrements MX [#1302](https://github.com/proconnect-gouv/federation/issues/1302).
- Suppression des champs `ipAddresses` inutilisés [#1308](https://github.com/proconnect-gouv/federation/issues/1308).
- Formatage du code source avec Prettier [#1309](https://github.com/proconnect-gouv/federation/issues/1309).
- Mise à jour de l'icône d'administration de FranceConnect à ProConnect [#1228](https://github.com/proconnect-gouv/federation/issues/1228).
- Mise à jour du label du champ email sur la page d'édition du SP [#1243](https://github.com/proconnect-gouv/federation/issues/1243).
