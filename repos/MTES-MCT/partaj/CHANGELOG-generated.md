## Changelog : partaj (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à Partaj au cours du dernier mois. Les modifications incluent des corrections de bugs pour améliorer l'expérience utilisateur, notamment sur l'affichage des saisines liées, ainsi que des mises à jour techniques importantes concernant le stockage des fichiers, l'authentification et la compatibilité avec les dernières versions de Django.

### Évolutions fonctionnelles
- Correction du bouton d'affichage des saisines liées [#IS-5](https://github.com/MTES-MCT/partaj/issues/IS-5).
- Ajout d'une modale pour la validation des pièces jointes.
- Ajout de modales de version.
- Correction d'un cas particulier concernant les "particuliers".

### Évolutions techniques
- Mise à jour de la méthode d'authentification vers `django_cas_ng`.
- Mise à jour de la version de Django.
- Refonte du système de stockage des fichiers : suppression de Whitenoise et utilisation de `partaj.core.storage.RelaxedCompressedStaticFilesStorage`.
- Correction de problèmes liés à la publication des données en base avant l'assignation de leur date de création.
- Suppression de la modale de confirmation de division et sauvegarde en cas de problème réseau.
- Mise à jour de la méthode `has_permission` vers `has_object_permission`.

### Autres changements
- Corrections de tests unitaires (problèmes de clés primaires manquantes, UUID invalides, récursivité, etc.).
- Améliorations du code (linting avec Black et Pylint).
- Correction de problèmes de style de code.
