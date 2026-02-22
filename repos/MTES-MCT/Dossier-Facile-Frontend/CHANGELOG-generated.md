## Changelog : Dossier-Facile-Frontend (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à Dossier-Facile-Frontend au cours des 30 derniers jours. Les principales évolutions concernent une refonte complète de la gestion des liens de partage, avec de nouvelles fonctionnalités comme la pause/réactivation de liens, la suppression, la création, et l'accès à des détails sur chaque lien. Des corrections d'accessibilité et des améliorations de l'interface utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Refonte complète de la page de partage des liens : nouvelle interface, gestion des liens OWNER et PARTNER, actions sur les liens (pause, suppression, modification). (#1867, #1869, #1802)
- Ajout d'un bouton pour mettre en pause les liens de partage. (#1861)
- Ajout d'une page de prévisualisation pour le dossier. (#1861)
- Amélioration de la gestion des fichiers non validés. (#1861)
- Possibilité de supprimer plusieurs liens de partage en même temps.
- Ajout d'un bouton pour copier le lien de partage.
- Affichage du nom d'utilisateur au lieu de l'adresse e-mail pour les locataires ayant le même nom.
- Correction d'un bug empêchant le fonctionnement des tests E2E suite à un ID invalide. (#1887)
- Correction de l'affichage des fichiers d'exemple. (#1873)
- Correction du formulaire de contact. (#1871)
- Correction de problèmes d'accessibilité sur le formulaire de locataire (#1852) et sur la page www (#1865).
- Correction d'un bug lié à l'affichage du message d'annonce pour les locataires. (#1868)
- Gestion des erreurs lors du chargement des liens de partage.
- Ajout d'un message d'erreur lors de la saisie d'une adresse e-mail trop longue.
- Amélioration de la navigation entre les onglets de la page de partage.

### Évolutions techniques
- Optimisation de l'appel à l'API pour le temps de traitement estimé. (#1877)
- Refactoring du code et suppression de code obsolète (suppression des anciennes pages de partage). (#1861)
- Utilisation des composants DSFR pour le sélecteur dans la page de partage.
- Amélioration de la structure des tests E2E pour éviter les duplications.
- Correction de code smells détectés par SonarQube.
- Mise à jour de la version de l'application à v3.4.0 et v3.4.5.

### Autres changements
- Correction de la documentation concernant le port du propriétaire. (#1849)
- Ajout de traçage (tracking) pour les actions sur les liens de partage.
- Ajout de commentaires et de TODOs pour faciliter le développement futur.
