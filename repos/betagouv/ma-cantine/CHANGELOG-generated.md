## Changelog : ma-cantine (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois-ci est marqué par une refonte majeure du processus de télédéclaration, désormais structuré sous forme de tunnel guidé pour faciliter la saisie des données. La sécurité de la plateforme a également été renforcée avec l'introduction de l'authentification à deux facteurs (2FA) pour les administrateurs, et les capacités d'analyse de données ont été consolidées grâce à l'intégration de nouveaux outils de modélisation (dbt).

### Évolutions fonctionnelles
- **Télédéclaration :**
    - Mise en place d'un nouveau tunnel de saisie structuré avec plusieurs étapes clés : sélection du mode de saisie ([#7051](https://github.com/betagouv/ma-cantine/issues/7051)), origine des produits ([#7055](https://github.com/betagouv/ma-cantine/issues/7055)), circuits courts et local ([#7056](https://github.com/betagouv/ma-cantine/issues/7056)), et couverture annuelle ([#7050](https://github.com/betagouv/ma-cantine/issues/7050)).
    - Ajout d'un volet "EGalim" simplifié ([#7053](https://github.com/betagouv/ma-cantine/issues/7053)) et d'écrans de récapitulatif avant validation ([#7102](https://github.com/betagouv/ma-cantine/issues/7102), [#7106](https://github.com/betagouv/ma-cantine/issues/7106)).
    - Amélioration de l'expérience utilisateur avec l'affichage des erreurs du bilan ([#7096](https://github.com/betagouv/ma-cantine/issues/7096)) et des informations de la cantine ([#7038](https://github.com/betagouv/ma-cantine/issues/7038)).
- **Établissement :** Création d'une page dédiée à la "Télédéclaration de l'année" ([#7020](https://github.com/betagouv/ma-cantine/issues/7020)).
- **Diagnostics :** Ajout de nouveaux indicateurs de provenance pour les données (France, Europe, circuit court, local) ([#7019](https://github.com/betagouv/ma-cantine/issues/7019), [#7021](https://github.com/betagouv/ma-cantine/issues/7021)).
- **Gestion des utilisateurs & Administration :**
    - Renforcement de la sécurité à l'inscription en bloquant les adresses emails jetables ([#7060](https://github.com/betagouv/ma-cantine/issues/7060)).
    - Amélioration des outils d'administration : nouveaux filtres (email confirmé, super-utilisateur, groupes) ([#7080](https://github.com/betagouv/ma-cantine/issues/7080)) et indicateur de présence d'un dispositif 2FA ([#7058](https://github.com/betagouv/ma-cantine/issues/7058)).

### Évolutions techniques
- **Sécurité :** Implémentation de l'authentification à deux facteurs (2FA) via TOTP pour les utilisateurs staff et superuser ([#7040](https://github.com/betagouv/ma-cantine/issues/7040), [#7046](https://github.com/betagouv/ma-cantine/issues/7046)).
- **Data & Analytics :** 
    - Création du projet dbt pour la modélisation des données destinée à Metabase ([#6421](https://github.com/betagouv/ma-cantine/issues/6421)).
    - Automatisation des tâches dbt via des processus asynchrones nocturnes ([#7118](https://github.com/betagouv/ma-cantine/issues/7118)) et intégration de tests de qualité SQL (sqlfluff) ([#7117](https://github.com/betagouv/ma-cantine/issues/7117)).
- **Backend & API :**
    - Refactorisation de la gestion du cache ([#7116](https://github.com/betagouv/ma-cantine/issues/7116)) et de l'organisation des paramètres de l'application ([#7033](https://github.com/betagouv/ma-cantine/issues/7033)).
    - Optimisation et séparation de l'endpoint d'achats `/summary` ([#7042](https://github.com/betagouv/ma-cantine/issues/7042)).
- **Infrastructure & Web :**
    - Migration du frontend vers `django-vite` pour améliorer le workflow de développement ([#7084](https://github.com/betagouv/ma-cantine/issues/7084)).
    - Optimisation du SEO via la gestion du sitemap et du fichier robots.txt ([#7111](https://github.com/betagouv/ma-cantine/issues/7111), [#7099](https://github.com/betagouv/ma-cantine/issues/7099)).
    - Correction de la configuration de stockage S3 suite à des mises à jour de dépendances ([#7039](https://github.com/betagouv/ma-cantine/issues/7039)).

### Autres changements
- **Documentation :** Mise à jour des instructions pour les agents d'IA (AGENTS.md) ([#7112](https://github.com/betagouv/ma-cantine/issues/7112)).
