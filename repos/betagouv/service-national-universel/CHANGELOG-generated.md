## Changelog : service-national-universel (30 derniers jours, au 10 mai 2024)

### Résumé
Ce changelog couvre les dernières améliorations apportées au Service National Universel, principalement axées sur la sécurité et la correction de bugs. Des mises à jour ont été effectuées pour renforcer la sécurité des mots de passe et de l'authentification, ainsi que pour corriger des erreurs affectant l'administration et l'API.

### Évolutions fonctionnelles
*   Amélioration de la gestion des convocations : Utilisation de données communes pour générer les convocations, améliorant ainsi la cohérence et l'efficacité du processus. [#3838](https://github.com/betagouv/service-national-universel/issues/3838)

### Évolutions techniques
*   Sécurité : Implémentation de la gestion de la variable d'environnement `JWT_SECRET` dans la configuration, renforçant la sécurité des jetons JWT.  Ajout de tests associés. [#5263](https://github.com/betagouv/service-national-universel/issues/5263)
*   Sécurité : Mise à jour de la librairie Mongoose vers la version 7.8.3 et alignement des dépendances pour corriger une vulnérabilité (CVE $where). [#5267](https://github.com/betagouv/service-national-universel/issues/5267)
*   Sécurité : Correction d'une vulnérabilité permettant de contourner le blocage de connexion en cas de mot de passe manquant. [#5264](https://github.com/betagouv/service-national-universel/issues/5264)
*   Sécurité : Renforcement de la sécurité des jetons de réinitialisation de mot de passe (utilisation de HMAC). [#5265](https://github.com/betagouv/service-national-universel/issues/5265)

### Autres changements
*   Corrections de bugs dans l'interface d'administration (Sentry) concernant la validation des bus PDT, la gestion des tableaux de bord vides et les sessions non définies.
*   Correction d'un bug dans l'API concernant l'export DSNJ et la cohérence des cohortes.
*   Correction d'un bug dans l'API concernant l'obtention du service départemental pour les modèles de convocation.
*   Amélioration de la gestion des types MIME inconnus lors de l'importation de fichiers.
*   Correction d'un bug dans Sentry lié à l'heure de rendez-vous.
*   Correction d'un problème de scrollbar dans le menu d'administration.
*   Amélioration du composant de message d'information dans l'administration.
