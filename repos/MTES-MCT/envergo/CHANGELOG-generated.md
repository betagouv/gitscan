## Changelog : envergo (30 derniers jours, au 25 août 2026)

### Résumé
Ce mois a été marqué par une mise à jour majeure de l'infrastructure technique pour améliorer la stabilité et la gestion des fichiers. Côté utilisateur, l'expérience a été enrichie par de nouveaux indicateurs visuels (badges d'urgence), une meilleure ergonomie sur mobile et une simplification des formulaires de vérification environnementale. La sécurité a également été renforcée pour protéger l'application contre les injections de données malveillantes.

### Évolutions fonctionnelles
- **Indicateurs visuels** : Ajout d'un badge "Urgence" dans les listes et résumés de dossiers pour faciliter le tri des priorités.
- **Ergonomie mobile** : Amélioration de la saisie des données relatives aux haies avec une interface adaptée aux écrans mobiles.
- **Simplification des formulaires** : 
    - Refonte des contrôles "Éviter / Réduire" avec une séparation des formulaires pour plus de clarté.
    - Amélioration de la gestion des procédures uniques lors du changement d'état.
- **Affichage et navigation** :
    - Intégration d'un nouveau composant de pagination (DSFR) [#1230](https://github.com/MTES-MCT/envergo/issues/1230).
    - Meilleure visibilité des échéances et des dates de projets non clôturés.
- **Contenu** : Mise à jour de la terminologie (wording) et des libellés pour une meilleure compréhension par les agents.

### Évolutions techniques
- **Sécurité** : Correction de vulnérabilités XSS par l'échappement systématique des données utilisateur et renforcement de la validation des entrées en backend [#1251](https://github.com/MTES-MCT/envergo/issues/1251).
- **Infrastructure & Déploiement** :
    - Mise à jour majeure de la stack d'hébergement (Scalingo, Node.js LTS et mise à niveau de GDAL) [#1252](https://github.com/MTES-MCT/envergo/issues/1252).
    - Refonte complète du système de stockage des fichiers via S3 et optimisation des chemins d'accès [#1253](https://github.com/MTES-MCT/envergo/issues/1253).
    - Optimisation de la configuration serveur avec l'installation de Nginx en amont de Gunicorn.
- **Performance** : Optimisation des requêtes de base de données, notamment pour la gestion des permissions et l'affichage des listes de dossiers, afin d'éviter les doublons de requêtes [#1241](https://github.com/MTES-MCT/envergo/issues/1241).

### Autres changements
- **Nettoyage** : Suppression de l'outil Gulp et simplification des scripts de build.
- **Documentation** : Amélioration de la documentation interne via l'ajout de docstrings.
