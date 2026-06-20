## Changelog : nitrates (30 derniers jours, au 09 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration significative de la calculatrice de nitrates, notamment l'ajout d'un calendrier dynamique et la gestion des périodes de calcul. L'interface d'administration a également été grandement améliorée, avec une refonte de la page d'accueil et une migration des référentiels vers la base de données pour une meilleure gestion et performance. Des corrections et améliorations ont été apportées à la gestion des cultures et des fertilisants.

### Évolutions fonctionnelles
- **Calculatrice:** Ajout d'un calendrier dynamique pour faciliter la saisie et la visualisation des dates de calcul. [#89, #96]
- **Calculatrice:** Généralisation de l'absorption des bornes adjacentes à une date saisie.
- **Calculatrice:** Possibilité de saisir des dates directement dans l'URL et de voir l'impact sur le calcul.
- **Calculatrice:** Gestion des conditions de période et des masques.
- **Interface d'administration:** Refonte complète de la page d'accueil avec accès rapide au simulateur et un diagramme Mermaid pour visualiser l'arbre de décision.
- **Interface d'administration:** Amélioration de l'UX pour la gestion des modèles de données et des référentiels.
- **Formulaire Culture:** Le formulaire de saisie des cultures est maintenant masqué jusqu'à ce qu'un clic soit effectué sur la carte.
- **Gestion des référentiels:** Migration des référentiels vers la base de données pour une meilleure gestion et performance.
- **Gestion des groupes de cultures:** Renommage de "CategorieCulture" en "GroupeCultureUI" et refactorisation des référentiels.

### Évolutions techniques
- **Base de données:** Création de modèles de base de données pour les référentiels et migration des données depuis le fichier YAML.
- **Tests:** Ajout de tests pour les nouvelles fonctionnalités et corrections de bugs.
- **Performance:** Optimisation de la performance de l'interface d'administration.
- **Refactoring:** Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- **Développement:** Utilisation de `watchdog/inotify` pour un autoreload fiable en développement.
- **Admin YAML:** Amélioration de l'éditeur YAML avec highlight et scroll.
- **Admin YAML:** Ajout de la possibilité de réordonner les branches par drag & drop.

### Autres changements
- **Documentation:** Mise à jour de la documentation pour refléter les changements apportés.
- **Nettoyage de code:** Suppression de code obsolète et amélioration de la qualité du code.
- **Corrections de bugs:** Correction de plusieurs bugs mineurs dans l'interface utilisateur et la logique de calcul.
- **Snapshot:** Création de snapshots de l'arbre de décision pour faciliter le suivi des modifications.
- **Grammaire:** Amélioration de la grammaire pour la calculatrice et les couverts d'interculture.
- **Viewer:** Modification des tags dans le viewer (retrait de 'culture' et renommage de 'sous-culture').
