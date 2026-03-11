## Changelog : mon-entreprise (30 derniers jours)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du comparateur de statuts, notamment en intégrant des informations plus précises sur la retraite et en simplifiant l'affichage des données. Des corrections de bugs ont également été apportées pour améliorer l'expérience utilisateur sur mobile et résoudre des problèmes d'affichage. Enfin, des refactorings techniques ont été réalisés pour préparer le projet à de futures évolutions, notamment une potentielle migration vers Next.js.

### Évolutions fonctionnelles
- Ajout d'un lien vers le simulateur de l'Assurance retraite dans le comparateur de statuts.
- Affichage de la valeur du point dans la section retraite complémentaire du comparateur.
- Remplacement des montants retraite par des informations sur les trimestres et les points acquis dans le comparateur.
- Correction de l'affichage mobile du montant des cotisations [#4290](https://github.com/betagouv/mon-entreprise/issues/4290).
- Ajout d'un message informant les utilisateurs des mises à jour 2026 pour le simulateur de salarié.
- Correction de la formule de calcul du RGDU.
- Ajout d'un lien vers le simulateur de l'Assurance retraite dans la section Droits Retraite.

### Évolutions techniques
- Refactorings importants pour préparer une potentielle migration vers Next.js :
    - Création d'un adaptateur de navigation pour gérer les routes et les paramètres.
    - Utilisation de hooks React Router pour accéder aux informations de navigation.
    - Suppression de code mort et de directives 'use client' inutiles.
    - Normalisation des noms de variables et amélioration de la structure du code.
- Amélioration de la gestion des conditions dans les composants DetailsRowCards.
- Amélioration du typage de certains composants de la librairie `logic-fabric`.
- Suppression de la fonction `inIframe` obsolète et remplacement par une approche basée sur le thème.
- Ajout de guards pour éviter les erreurs lors de l'accès à `window` dans l'environnement serveur.
- Correction d'un typo et d'un import implicite dans la librairie `logic-fabric`.

### Autres changements
- Mise à jour de l'Acre.
- Hausse de la CSG non déductible sur dividendes soumises au barème.
- Correction de l'affichage du séparateur dans le comparateur (espace insécable avant le deux-points).
- Correction du format d'affichage de la valeur du point (remplacement de "€/an" par "€ par an").
- Suppression du lien vers le simulateur Cnav du comparateur.
- Suppression de l'objectif retraite de base de la configuration du comparateur.
- Suppression des objectifs de projection retraite base et complémentaire de la configuration PL.
- Correction d'un typo "Embeded" -> "Embedded" dans plusieurs fichiers.
- Ajout de commentaires pour référencer des issues (ex: #4323).
- Amélioration de la documentation concernant les droits à la retraite.
- Application du formatage Prettier.
- Ajout de nouveaux composants minimalist dans `logic-fabric` (ToggleGroup, YesOrNoToggleGroup, RadioGroup).
