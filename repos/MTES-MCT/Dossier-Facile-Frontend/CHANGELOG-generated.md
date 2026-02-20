## Changelog : Dossier-Facile-Frontend (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à Dossier-Facile-Frontend au cours des 30 derniers jours. Les principales évolutions concernent une refonte majeure de la gestion des liens de partage, avec une nouvelle page dédiée, des fonctionnalités de pause/réactivation, de suppression et d'édition. Des corrections d'accessibilité et des améliorations de l'expérience utilisateur ont également été apportées.

### Évolutions fonctionnelles
- **Gestion des liens de partage :** Nouvelle page `/partages` pour gérer les liens de partage (création, suppression, édition, pause/réactivation). (#1867, #1866, #1852)
- **Partage de fichiers :** Ajout de la possibilité de télécharger un PDF associé à un lien de partage. (#1867)
- **Actions sur les liens :** Ajout de sections d'actions (copier le lien, modifier, etc.) pour les liens de partage. (#1867)
- **Affichage du nom d'utilisateur :** Affichage du nom d'utilisateur au lieu de l'adresse e-mail dans l'interface locataire. (#1234)
- **Amélioration de la page de prévisualisation :** Ajout d'une page de prévisualisation pour le dossier. (#1861)
- **Gestion des fichiers non validés :** Gestion des fichiers non validés. (#1861)
- **Correction d'un bug :** Correction d'un bug empêchant le fonctionnement des tests E2E suite à un ID invalide. (#1887)
- **Correction d'un bug :** Correction d'un problème lié à la page de partage lorsque le dossier des colocataires n'est pas entièrement complété. (#1884)
- **Correction d'un bug :** Correction de l'affichage des messages d'annonce dans l'interface locataire. (#1868)
- **Correction d'un bug :** Correction de l'affichage des dates des liens partagés. (#1867)
- **Correction d'un bug :** Correction d'un problème d'accessibilité sur la page d'accueil. (#1865)
- **Correction d'un bug :** Correction d'un problème d'accessibilité sur le formulaire locataire. (#1852)
- **Correction d'un bug :** Correction d'un bug lié à un formulaire de contact. (#1871)
- **Correction d'un bug :** Correction d'un bug lié à des fichiers d'exemple. (#1873)

### Évolutions techniques
- **Refactorisation :** Refactorisation du code pour améliorer la qualité et la maintenabilité.
- **Tests E2E :** Ajout et amélioration des tests E2E pour la page de partage. (#1867)
- **Mise à jour des dépendances :** Mise à jour de certaines dépendances du projet. (#1812, #1851)
- **Amélioration de l'accessibilité :** Améliorations générales de l'accessibilité de l'application. (#1865, #1850)
- **Optimisation des performances :** Optimisation de l'appel à l'API pour le temps de traitement estimé. (#1877)

### Autres changements
- **Documentation :** Correction de la documentation concernant le port du propriétaire. (#1849)
- **Nettoyage de code :** Suppression de code obsolète et nettoyage général du code.
- **Bump de version :** Passage en version 3.3.7 et 3.4.0 puis 3.4.5.
