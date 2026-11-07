## Changelog : acceslibre (30 derniers jours, au 05 novembre 2026)

### Résumé
Ce mois-ci, la plateforme s'enrichit de nouveaux outils, notamment un widget dédié au secteur de la santé et des fonctionnalités améliorées pour les tribunes. L'expérience utilisateur a été optimisée, particulièrement lors de l'utilisation de l'outil de visualisation Panoramax. Parallèlement, d'importants travaux ont été menés pour renforcer la sécurité, la performance et la stabilité de l'infrastructure.

### Évolutions fonctionnelles
- **Nouveaux outils et fonctionnalités** :
    - Ajout d'un nouveau widget pour le secteur de la santé [#2923](https://github.com/MTES-MCT/acceslibre/issues/2923).
    - Amélioration du système de "tribunes" avec la gestion des questions parentes et une meilleure compatibilité ascendante [#2936](https://github.com/MTES-MCT/acceslibre/issues/2936).
- **Optimisation de l'expérience utilisateur** :
    - Amélioration de l'outil de visualisation Panoramax : correction du nombre de photos affichées [#2949](https://github.com/MTES-MCT/acceslibre/issues/2949) et mise à jour du comportement des fenêtres modales [#2951](https://github.com/MTES-MCT/acceslibre/issues/2951).
    - Correction de la logique de recherche pour éviter les faux positifs sur les mots contenant des tirets [#2937](https://github.com/MTES-MCT/acceslibre/issues/2937).
    - Correction de l'affichage du widget de la documentation API [#2912](https://github.com/MTES-MCT/acceslibre/issues/2912).
- **Confidentialité et protection des données** :
    - Sécurisation des formulaires en empêchant l'exposition d'informations d'accessibilité non prévues [#2940](https://github.com/MTES-MCT/acceslibre/issues/2940).

### Évolutions techniques
- **Performance et optimisation** :
    - Réduction des temps de réponse via la suppression de requêtes SQL redondantes (problème de N+1 queries) [#2884](https://github.com/MTES-MCT/acceslibre/issues/2884).
    - Optimisation du chargement des ressources (bundles) pour Panoramax [#2938](https://github.com/MTES-MCT/acceslibre/issues/2938).
- **Sécurité et API** :
    - Renforcement de la sécurité de l'API : corrections sur Swagger [#2915](https://github.com/MTES-MCT/acceslibre/issues/2915) et amélioration de la gestion des clés API [#2909](https://github.com/MTES-MCT/acceslibre/issues/2909).
    - Mise en conformité de la politique de sécurité du contenu (CSP) pour Panoramax [#2952](https://github.com/MTES-MCT/acceslibre/issues/2952).
    - Mise à jour et enrichissement des schémas de réponse de l'API [#2939](https://github.com/MTES-MCT/acceslibre/issues/2939) et [#2925](https://github.com/MTES-MCT/acceslibre/issues/2925).
- **Infrastructure et Environnement** :
    - Mise à jour majeure de l'environnement de développement et de production (Docker, Python 3.14.8) [#2911](https://github.com/MTES-MCT/acceslibre/issues/2911), [#2922](https://github.com/MTES-MCT/acceslibre/issues/2922).
    - Amélioration des scripts de restauration de données via Docker [#2885](https://github.com/MTES-MCT/acceslibre/issues/2885).

### Autres changements
- **Nettoyage et maintenance** :
    - Suppression de l'ancienne version de la contribution (contrib v2) [#2886](https://github.com/MTES-MCT/acceslibre/issues/2886).
    - Traduction des champs de versioning [#2953](https://github.com/MTES-MCT/acceslibre/issues/2953).
