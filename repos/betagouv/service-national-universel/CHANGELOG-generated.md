## Changelog : service-national-universel (30 derniers jours, au 10 mai 2024)

### Résumé
Ce changelog présente les améliorations apportées au Service National Universel au cours des 30 derniers jours. Les principales évolutions concernent la sécurité de la réinitialisation des mots de passe, la gestion des accès et la robustesse de l'API, notamment pour l'export de données et la génération de convocations. Des corrections de bugs ont également été implémentées dans l'interface d'administration.

### Évolutions fonctionnelles
- **Support :** Amélioration de la sécurité lors de la réinitialisation des mots de passe en utilisant le hachage des tokens de réinitialisation avec HMAC [#5265](https://github.com/betagouv/service-national-universel/issues/5265).
- **Support :** Blocage de la connexion pour les utilisateurs n'ayant pas renseigné leur mot de passe [#5264](https://github.com/betagouv/service-national-universel/issues/5264).
- **API :** Amélioration de la gestion des secrets JWT (JSON Web Token) pour renforcer la sécurité de l'API [#5263](https://github.com/betagouv/service-national-universel/issues/5263).
- **API :** Amélioration de la génération des convocations en utilisant des données communes aux jeunes [#3838](https://github.com/betagouv/service-national-universel/issues/3838).

### Évolutions techniques
- **API :** Correction d'un bug concernant les CRONs d'export de données DSNJ, où l'ID du centre était parfois indéfini [#3839](https://github.com/betagouv/service-national-universel/issues/3839).
- **API :** Correction d'un bug dans l'export DSNJ concernant la cohérence entre la cohorte de jeunes et la cohorte de session [#3849](https://github.com/betagouv/service-national-universel/issues/3849).

### Autres changements
- **Admin :** Corrections de bugs et améliorations de l'interface d'administration concernant l'affichage des données et la gestion des erreurs (Sentry) :
    - Correction de la validation du bus PDT. [#3842](https://github.com/betagouv/service-national-universel/issues/3842)
    - Gestion de l'affichage du tableau de bord "todo" lorsqu'il est vide. [#3843](https://github.com/betagouv/service-national-universel/issues/3843)
    - Correction d'un problème lié à la session du centre d'appel. [#3835](https://github.com/betagouv/service-national-universel/issues/3835)
- **API :** Suppression de la récupération du service départemental pour le modèle de convocation.
- **API :** Gestion des types MIME inconnus lors de l'import de fichiers [#3825](https://github.com/betagouv/service-national-universel/issues/3825).
- **Sentry :** Correction d'un cas où l'heure de la réunion était nulle [#3840](https://github.com/betagouv/service-national-universel/issues/3840).
- **Admin :** Correction de la barre de défilement du menu [#3823](https://github.com/betagouv/service-national-universel/issues/3823).
- **Admin :** Correction du composant de message d'information et de la gestion des filtres vides [#3830](https://github.com/betagouv/service-national-universel/issues/3830).
