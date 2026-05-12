## Changelog : aides-agri (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la préparation et le déploiement de la version 2 du parcours agri, avec des améliorations significatives de l'interface utilisateur et de la gestion des données. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des mises à jour de sécurité et de dépendances.

### Évolutions fonctionnelles
- **Parcours agri v2 :** Déploiement de la nouvelle version du parcours utilisateur pour les exploitants agricoles [#418].
- **Filtres sur la page d'aides :** Possibilité de sélectionner toutes les filières sur la page d'ensemble des aides [#531].
- **Informations sur les aides :** Ajout d'une information sur les aides réservées aux groupements de producteurs [#538].
- **Export CSV (Admin) :** Ajout de la raison de désactivation lors de l'export CSV des aides dans l'interface d'administration [#532].
- **Améliorations de l'outil d'édition :** Améliorations générales de l'outil d'édition des aides [#498].
- **Base juridique des aides :** Consolidation de la gestion de la base juridique des aides [#495, #499, #504].
- **Logos DDT(M) :** Ajout de scripts pour la création et l'association des logos des Directions Départementales des Territoires et de la Mer [#493].

### Évolutions techniques
- **Performance :** Tentatives de réduction des latences de l'application et de limitation des fuites mémoire [#523, #537].
- **Connexion BDD :** Correction du réglage de la connexion persistante à la base de données [#536].
- **Gestion des schémas BDD :** Facilitation du déploiement en cas de changement de schéma de la base de données [#501].
- **Accessibilité :** Amélioration de l'accessibilité de la validation de formulaire côté client [#530].
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances, notamment Django, django-dsfr, htmx.org, faker, et sentry-sdk (voir commits individuels).
- **Uv lock :** Mise à jour et verrouillage des dépendances avec `uv` [#522, #491, #490].

### Autres changements
- **Statistiques publiques :** Mise à jour des statistiques publiques pour avril 2026 [#533].
- **Security.txt :** Mise à jour de la date de validité du fichier security.txt [#505].
- **Correction PDF :** Correction d'un bug d'impression PDF [#525].
- **Correction historique (Admin) :** Correction d'un crash de l'historique dans l'interface d'administration [#524].
- **Tracking Matomo :** Ajout du tracking d'événement de clic sur lien externe pour le mode minimal [#535].
- **Corrections d'affichage :** Correction de bugs d'affichage de couleur sur la page de résultats [#511].
- **Corrections mineures :** Diverses corrections mineures et ajustements [#502, #503, #515].
