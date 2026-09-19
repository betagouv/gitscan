# Synthèse d'activité : france-connect (du 11/05 au 18/05)

## Résumé de l'activité
L'activité de cette période a principalement visé l'amélioration de l'expérience utilisateur et la préparation des futures évolutions de l'écosystème. Les utilisateurs bénéficient d'un tableau de bord plus ergonomique (notamment sur mobile), d'un meilleur accompagnement en cas d'erreur et de messages de prévention lors de la gestion des identifiants. Par ailleurs, l'intégration visuelle du futur IdP Yris et l'ouverture via l'eIDASBridge préparent l'extension des services et la connectivité de nouveaux prestataires [sources](/repos/france-connect/sources).

## Sécurité
- Renforcement de l'isolation réseau par la séparation des consommateurs MongoDB selon le niveau d'assurance (faible ou élevé).
- Amélioration de la traçabilité et de la capacité de diagnostic grâce à l'ajout de la source IP et du port client dans les journaux métier [sources](/repos/france-connect/sources).

## Autres changements notables
- Refactorisation de l'architecture logicielle pour optimiser le partage de code entre les différentes applications.
- Renforcement de l'observabilité via l'implémentation de logs métier et de contrôles de cache sur les routes de métadonnées.
- Optimisation de la confidentialité des données par la suppression de claims inutilisés ("phone_number" et "address") [sources](/repos/france-connect/sources).

## Dépôts les plus actifs
- [sources](/repos/france-connect/sources) : Amélioration de l'ergonomie utilisateur, renforcement de la sécurité réseau et optimisation de la maintenance technique.
