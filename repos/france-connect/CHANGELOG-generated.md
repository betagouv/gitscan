# Synthèse d'activité : france-connect (du 11/05 au 18/05)

## Résumé de l'activité
L'activité de cette période a principalement visé à fluidifier le parcours des utilisateurs et à renforcer l'assistance. Des améliorations ergonomiques sur le tableau de bord mobile et l'ajout de liens de support direct sur les pages d'erreur permettent de réduire la friction en cas de difficulté. Par ailleurs, l'écosystème se prépare à l'arrivée de nouveaux acteurs avec l'intégration visuelle du futur IdP Yris [sources](/repos/france-connect/sources).

## Sécurité
- Amélioration de l'isolation réseau via la séparation des consommateurs MongoDB selon le niveau d'assurance [sources](/repos/france-connect/sources).
- Possibilité de connecter des prestataires de services ayant des exigences de sécurité spécifiques via l'eIDASBridge [sources](/repos/france-connect/sources).
- Ajout d'un message d'avertissement de sécurité lorsqu'un utilisateur tente de désactiver l'ensemble de ses identifiants [sources](/repos/france-connect/sources).

## Autres changements notables
- Optimisation de la traçabilité grâce à l'ajout de logs métier détaillés (incluant l'IP et le port client) pour le tableau de bord et FranceConnect+ [sources](/repos/france-connect/sources).
- Refactorisation de la structure des dossiers pour favoriser le partage de code entre les applications [sources](/repos/france-connect/sources).
- Nettoyage des données transmises avec la suppression de certains champs (claims) inutilisés [sources](/repos/france-connect/sources).
- Renforcement de la qualité logicielle par l'ajout de tests BDD sur les notifications et l'historique de connexion [sources](/repos/france-connect/sources).

## Dépôts les plus actifs
- [sources](/repos/france-connect/sources) : Amélioration de l'expérience utilisateur, de la traçabilité et de l'architecture technique.
