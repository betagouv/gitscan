## Changelog : code-du-travail-numerique (30 derniers jours)

### Résumé
Ce mois-ci, le projet a bénéficié d'améliorations significatives de la recherche, de l'accessibilité et de l'expérience utilisateur. Des corrections de bugs ont été apportées pour assurer la stabilité et la fiabilité de la plateforme, notamment au niveau des tests et de l'intégration continue. De nouvelles fonctionnalités ont été ajoutées, comme un formulaire de sondage sur les accords d'entreprise et des améliorations de l'interface utilisateur pour les modèles de documents et la page d'accueil.

### Évolutions fonctionnelles
- Amélioration de la recherche avec des résultats plus pertinents et une meilleure expérience utilisateur (#7107)
- Ajout d'un formulaire pour le sondage sur les accords d'entreprise (#7121)
- Changement de la phrase d'accroche pour le questionnaire sur les accords d'entreprise (#7126)
- Amélioration de la gestion des listes et des informations dans la page des modèles de documents (#7117)
- Ajout d'une question pour valider la pertinence des résultats de recherche (#7115)
- Ajout de nouvelles icônes pour les thèmes et correction de problèmes d'accessibilité (#7094)
- Amélioration de la zone de clic sur la page "La hiérarchie des textes" (#7090)
- Amélioration de la popup de recherche en termes d'accessibilité (#7089)
- Fermeture de la popup de recherche lors du changement de lien (#7083)
- Suppression des questions "cul de sac" dans les outils (#7079)
- Nouveau design pour les pages thèmes (#7073)

### Évolutions techniques
- Optimisation du temps de build Docker (#7122)
- Mise à jour vers la dernière version de Next.js (#7095)
- Ajout d'un hash d'intégrité pour l'intégration du script des widgets (#7076)
- Normalisation du widget "Indemnité de rupture conventionnelle" dans le CI (#7112)
- Amélioration des tests E2E pour assurer une couverture complète et une exécution stable (#7114, #7124)
- Ajout de l'audit Lighthouse et mise en place d'un CI manuel pour l'exécuter (#7074)
- Ajout du support des JSON-LD pour améliorer le référencement et l'accessibilité (#7071)
- Utilisation de la recherche v2 par défaut (#7077)

### Autres changements
- Suppression du fichier de configuration CodeQL (#7114)
- Ajout d'un message sur Mattermost après une release (#7080)
- Correction de la redirection pour les conventions collectives 1031 et 3203 (#7109)
