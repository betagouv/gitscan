## Changelog : drive (30 derniers jours, au 24/09/2026)

### Résumé
Ce mois-ci, le projet a introduit une gestion beaucoup plus flexible des restrictions d'accès, permettant de sécuriser ou de libérer des dossiers par simple déplacement dans l'arborescence. Ces évolutions s'accompagnent d'une optimisation majeure de la performance du moteur de permissions et d'une modernisation de l'infrastructure de stockage locale.

### Évolutions fonctionnelles
- **Gestion des accès et restrictions** : 
    - Nouveau système permettant de restreindre ou de lever une restriction sur un dossier par simple déplacement (attachement/détachement) dans l'arborescence.
    - Les dossiers restreints sont désormais masqués de la vue principale et exclus des résultats de recherche et des exports.
    - Possibilité de cibler d'autres éléments pour appliquer des restrictions.
- **Sécurité et droits** : Renforcement du contrôle des droits d'upload pour la création de documents à la racine du drive.
- **Interface utilisateur** : 
    - Amélioration du rendu des fichiers PDF (gestion des polices et des décodeurs).
    - Correction de la gestion des langues du navigateur et rafraîchissement automatique de la vue "Récents" après modification d'un élément.

### Évolutions techniques
- **Infrastructure et stockage** : 
    - Remplacement de MinIO par RustFS pour le stockage d'objets en environnement local.
    - Mise à jour des déploiements Helm pour permettre la configuration de variables d'environnement spécifiques au backend.
- **Backend et Performance** : 
    - Refonte profonde du moteur de permissions pour une gestion plus modulaire des capacités et des rôles.
    - Optimisation de la vitesse de recherche des ancêtres dans l'arborescence.
    - Mise en place d'un pool de connexions PostgreSQL (`psycopg_pool`) pour améliorer la gestion de la base de données.
- **Qualité et Observabilité** : 
    - Ajout d'une suite de tests de charge avec JMeter (scénarios de sessions utilisateurs et de lecture intensive).
    - Intégration du monitoring de performance via Sentry.
    - Amélioration de l'environnement de tests de bout en bout (E2E).
- **Développement** : Optimisation du processus de build des dépendances frontend via conteneur et amélioration des règles Makefile.

### Autres changements
- **Documentation** : Mise à jour du README (ajout de badges) et documentation technique des paramètres de permissions du backend.
- **Maintenance** : Nettoyage des variables d'environnement inutilisées et gestion des versions de release (0.22.0 et 0.23.0).
