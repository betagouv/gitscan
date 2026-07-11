## Changelog : portail-rse (30 derniers jours, au 09 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration significative de la fonctionnalité d'exportation des données VSME au format PowerPoint (pptx). De nombreuses corrections et optimisations ont été apportées pour assurer un rendu précis et complet des informations, en tenant compte des différents cas de figure (indicateurs pertinents, non pertinents, non applicables). Des améliorations ont également été apportées à l'administration et à la sécurité.

### Évolutions fonctionnelles
- Possibilité de réinitialiser un indicateur VSME [#2a12381](https://github.com/betagouv/portail-rse/commit/2a12381).
- Amélioration de l'exportation au format PPTX pour les indicateurs VSME :
    - Gestion des indicateurs non pertinents et non applicables.
    - Export des totaux de l'indicateur C3.
    - Affichage correct de la couverture.
    - Gestion des tableaux à lignes variables et fixes.
    - Ajout d'indicateurs environnementaux.
    - Centrage du contenu des cellules.
    - Gestion des nombres entiers et des choix multiples.
    - Ajout d'informations sur la couverture (nom de l'entreprise).
    - Amélioration du sommaire.
    - Correction de l'alignement de l'image de fond sur certaines diapositives.
- Ajout d'un lien de téléchargement pour le rapport PPTX.
- Recherche par ensemble d'ID d'utilisateurs dans l'administration [#0b826a1](https://github.com/betagouv/portail-rse/commit/0b826a1).
- Nettoyage du compte utilisateur de test pour les personnes sans compte Proconnect [#f910a2b](https://github.com/betagouv/portail-rse/commit/f910a2b).
- Empêchement de la modification du profil et du mot de passe de l'utilisateur test [#4df6290](https://github.com/betagouv/portail-rse/commit/4df6290), [#42bcad5](https://github.com/betagouv/portail-rse/commit/42bcad5).
- Ajout de logs pour les requêtes d'export xlsx et pptx [#260e6ff](https://github.com/betagouv/portail-rse/commit/260e6ff).

### Évolutions techniques
- Mise à jour de Django de la version 5.1.15 à la version 5.2.16 [#48eb2fc](https://github.com/betagouv/portail-rse/commit/48eb2fc).
- Mise à jour de Node.js dans `package.json` et l'intégration continue [#376ab90](https://github.com/betagouv/portail-rse/commit/376ab90).
- Refactoring de l'administration : suppression d'une définition d'attribut en trop [#8adeba0](https://github.com/betagouv/portail-rse/commit/8adeba0).
- Refactoring de la commande de renommage pour une action élargie [#b5f630c](https://github.com/betagouv/portail-rse/commit/b5f630c).
- Simplification et changements de signature des fonctions d'export PPTX.
- Suppression des éléments liés aux modules complets dans l'export PPTX.
- Amélioration de la gestion des erreurs lors de la suppression de schémas.
- Correction d'une erreur d'affichage de la dernière diapo pour C2-48.

### Autres changements
- Documentation : Complétion du diagramme overview [#46d3b7e](https://github.com/betagouv/portail-rse/commit/46d3b7e).
- Mise à jour des dépendances : `cryptography`, `aiohttp`, `pyjwt`, `joserfc` (mises à jour automatiques).
