## Changelog : catalogi (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à catalogi au cours des 30 derniers jours. Les principales évolutions concernent l'import de métadonnées depuis GitLab et GitHub, ainsi que des corrections de bugs et des améliorations de l'interface utilisateur. Des migrations de données ont également été effectuées pour optimiser la gestion des versions des logiciels.

### Évolutions fonctionnelles
- Ajout de l'import de données depuis les référentiels GitLab (#291).
- Amélioration de l'affichage des métadonnées des dépôts GitHub, incluant l'activité partielle du dépôt (#203).
- Correction d'une traduction française incorrecte pour le nombre d'instances publiques (#203).
- Correction de l'affichage de l'interface utilisateur (#338).
- Migration des routes web pour utiliser l'ID du logiciel au lieu de son nom (#7be2371).
- Ajout d'options de configuration de l'interface utilisateur (#203).
- Mise à jour du type lors de l'import de métadonnées depuis GitHub (#291).

### Évolutions techniques
- Migration de la colonne `versionMin` vers les attributs personnalisés pour une meilleure flexibilité.
- Refactoring du code pour supprimer le code mort et améliorer la lisibilité.
- Amélioration de la gestion des liens externes obsolètes lors de la mise à jour des données.
- Correction de l'utilisation des variables d'environnement au niveau bas du code.
- Suppression de l'utilisation de `dotenv` dans les tests.
- Correction de problèmes liés au chargement du token GitHub.
- Déplacement de la fonction `castToSoftwareExternalData` vers un fichier plus pertinent.
- Amélioration de la gestion des appels à l'API GitHub pour la récupération des métadonnées des dépôts (#292).

### Autres changements
- Ajout d'un fichier de documentation (ignoré par Git).
- Augmentation du numéro de version de l'application.
- Correction de bugs mineurs et amélioration de la stabilité générale.
