## Changelog : complements-alimentaires (30 derniers jours, au 16 septembre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur la fiabilisation du parcours de visa (automatisation de certains champs et correction d'erreurs d'affichage) et l'amélioration de la qualité des données exportées. Des optimisations techniques ont également été réalisées pour rendre l'envoi d'e-mails plus fluide et renforcer la sécurité de la plateforme.

### Évolutions fonctionnelles
- **Gestion des visas** : 
    - Mise en place de valeurs par défaut automatiques pour faciliter la saisie des visas.
    - Correction d'erreurs 404 sur les pages d'instruction et de visa survenant lorsqu'aucun auteur n'est renseigné pour une déclaration.
    - Intégration de la gestion des jours de retard de visa [#3105](https://github.com/betagouv/complements-alimentaires/pull/3105).
- **Données & Open Data** :
    - Correction du vocabulaire utilisé dans les exports de données Open Data pour une meilleure précision.
    - Évolution du jeu de données ETL concernant les décisions [#3115](https://github.com/betagouv/complements-alimentaires/pull/3115).
- **Corrections de bugs** :
    - Résolution d'un problème bloquant lors de la vérification de l'adresse e-mail [#3095](https://github.com/betagouv/complements-alimentaires/pull/3095).
- **Interface utilisateur** :
    - Mise à jour des composants graphiques (charts) via le Design System (DSFR) [#3073](https://github.com/betagouv/complements-alimentaires/pull/3073).

### Évolutions techniques
- **Performance & Backend** :
    - Passage en mode asynchrone pour l'envoi d'e-mails via Brevo afin d'améliorer la réactivité du système [#3074](https://github.com/betagouv/complements-alimentaires/pull/3074).
- **Authentification** :
    - Mise à jour et intégration du composant ProConnect [#3023](https://github.com/betagouv/complements-alimentaires/pull/3023).

### Autres changements
- **Sécurité** : Ajout du fichier `security.txt` pour faciliter le signalement de vulnérabilités [#3106](https://github.com/betagouv/complements-alimentaires/pull/3106).
- **Documentation** : Ajout de nouvelles documentations pour le projet.
- **Qualité de code** : Mise à jour de la configuration de l'outil de linting vers ESLint 10.
