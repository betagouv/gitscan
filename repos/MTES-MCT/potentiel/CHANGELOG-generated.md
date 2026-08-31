## Changelog : potentiel (30 derniers jours, au 28/08/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'amélioration de la fiabilité des données et la fluidification des processus d'importation. Des ajustements importants ont été apportés à la gestion des projets (règles de puissance, nouvelles périodes) et à l'interface utilisateur pour offrir une expérience plus cohérente et intuitive aux professionnels.

### Évolutions fonctionnelles
- **Gestion des imports et données** : Amélioration de l'import des coordonnées depuis la DN [#4520], mise à jour des règles CSV pour les instructions DN [#4527] et possibilité de rendre la note totale optionnelle lors de l'import des candidats [#4518].
- **Nouvelles règles et fonctionnalités** : Application de règles sur la puissance maximale par famille et le volume réservé pour les modifications administratives [#4522], ajout de la période "P12 Eolien" [#4519] et création d'un nouvel endpoint pour transmettre les dates d'achèvement par lot [#4493].
- **Interface utilisateur (UI)** : Déplacement des titres de page au-dessus du contenu [#4502], uniformisation des messages d'erreur lors de modifications identiques [#4511] et adaptation de la synthèse de période selon le type (lauréat ou candidature) [#4508].
- **Corrections de bugs** : Résolution de problèmes liés aux gestionnaires de réseau inconnus [#4521], blocage de la modification des dossiers de raccordement sur les projets achevés [#4515] et correction d'un bug sur l'utilisation des dates d'accord dans les fichiers [#4506].

### Évolutions techniques
- **Maintenance des données** : Plusieurs mises à jour des dumps de données (statistiques publiques, tâches de raccordement, adresses de gestionnaires de réseau) pour garantir l'exactitude des informations système [#4526, #4523, #4528, #4516, #4510, #4503].
- **Architecture et composants** : Refactorisation de la page historique en composants testables [#4509] et migration des alertes vers le composant standard DSFR Notice [#4513].
- **Sécurité** : Mise à jour de Next.js et PostCSS pour corriger des vulnérabilités identifiées lors des audits de sécurité [#4514].
