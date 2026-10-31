# Synthèse d'activité : france-connect (du 11/05 au 18/05)

## Résumé de l'activité
L'activité récente de FranceConnect s'est concentrée sur l'amélioration de l'expérience utilisateur et l'élargissement des capacités de connexion. Des optimisations majeures ont été apportées au tableau de bord utilisateur, notamment pour une utilisation mobile plus fluide et une meilleure gestion des sessions. L'écosystème s'enrichit également avec l'intégration de nouveaux partenaires (IdP Yris) et une capacité accrue à connecter des prestataires via l'eIDASBridge [sources](/repos/france-connect/sources).

## Sécurité
- Renforcement de l'isolation réseau par la séparation des consommateurs MongoDB selon le niveau d'assurance (faible ou élevé) [sources](/repos/france-connect/sources).
- Réduction de l'exposition de données personnelles par la suppression de claims inutilisés (numéro de téléphone et adresse) dans FranceConnect+ [sources](/repos/france-connect/sources).

## Autres changements notables
- Refactorisation de l'architecture technique (hiérarchie des dossiers React) pour favoriser le partage de code entre les différentes applications [sources](/repos/france-connect/sources).
- Amélioration significative de la traçabilité et du diagnostic grâce à l'implémentation de nouveaux logs métier détaillés (incluant l'IP et le port client) [sources](/repos/france-connect/sources).
- Renforcement de la fiabilité du système via l'ajout de tests BDD (Behavior Driven Development) sur les notifications et l'historique de connexion [sources](/repos/france-connect/sources).

## Dépôts les plus actifs
- [sources](/repos/france-connect/sources) : Évolutions centrées sur l'expérience utilisateur, la sécurité des données et la robustesse de l'infrastructure.
