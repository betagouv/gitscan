# Synthèse d'activité : france-connect (du 11/05 au 18/05)

## Résumé de l'activité
L'activité de la semaine s'est concentrée sur l'amélioration de l'expérience utilisateur et de l'accessibilité du service. Des optimisations majeures ont été apportées au tableau de bord, notamment pour une utilisation mobile plus fluide et une meilleure gestion des sessions. L'écosystème s'enrichit également avec l'intégration visuelle de l'IdP Yris et une meilleure prise en charge des prestataires via l'eIDASBridge [sources](/repos/france-connect/sources).

## Sécurité
- Réduction de l'exposition des données personnelles par la suppression de claims inutilisés ("phone_number" et "address") dans FranceConnect+ [sources](/repos/france-connect/sources).

## Autres changements notables
- **Amélioration de l'observabilité** : Ajout de logs métier détaillés (incluant l'IP et le port client) pour faciliter le diagnostic et le suivi des utilisateurs [sources](/repos/france-connect/sources).
- **Optimisation de l'infrastructure** : Séparation des consommateurs MongoDB par niveau d'assurance pour renforcer l'isolation réseau [sources](/repos/france-connect/sources).
- **Évolutions techniques et architecture** : Refactorisation de la structure des dossiers pour optimiser le partage de code React et préparation du futur tableau de bord partenaire par le déplacement de composants dédiés [sources](/repos/france-connect/sources).

## Dépôts les plus actifs
- [sources](/repos/france-connect/sources) : Amélioration de l'interface utilisateur, de la traçabilité et de l'architecture technique.
