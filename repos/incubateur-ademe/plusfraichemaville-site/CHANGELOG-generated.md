## Changelog : plusfraichemaville-site (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur de l'espace projet, notamment concernant le module ClimaDiag et la gestion des fiches solutions. Des ajustements ont également été apportés pour simplifier le parcours utilisateur et supprimer des éléments non pertinents, comme les notifications et certains chargements inutiles sur la page d'accueil.

### Évolutions fonctionnelles
- Le menu déroulant de maturité est maintenant affiché correctement [#504](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/504).
- Suppression de l'appel à l'iframe Connect sur la page d'accueil pour améliorer la performance et la simplicité [#503](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/503).
- Ajout d'une redirection pour les utilisateurs venant de MCP PGE [#502](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/502).
- Suppression de la fiche solution "matériaux à changement de phase" de l'espace projet [#501](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/501).
- Ajout d'un bouton secondaire pour les cartes de webinaires [#500](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/500).
- Modification de la légende pour ClimaDiag dans l'espace projet [#499](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/499).
- Mise à jour des canaux d'acquisition [#498](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/498).
- Amélioration de la gestion des caractères spéciaux dans la recherche ClimaDiag [#497](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/497).
- Suppression de la mention "non disponible en outre-mer" pour ClimaDiag [#493](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/493).
- Filtrage des résultats des aides territoires qui ne sont pas "live" [#495](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/495).

### Évolutions techniques
- Utilisation du paramètre `is_live` pour filtrer les données [#495](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/495).
- Correction de l'utilisation du seuil ClimaDiag pour assurer une cohérence [#494](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/494).
- Mise à jour des dépendances du projet [#496](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/496).
- Correction de l'alignement du bouton "NL" [#504](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/504).
- Suppression de l'envoi de mails pour les retours d'expérience (REX) [#503](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/503).

### Autres changements
- Correction de fautes de frappe.
- Amélioration de la lisibilité du code avec Prettier.
- Importation du script ClimaDiag corrigé.
