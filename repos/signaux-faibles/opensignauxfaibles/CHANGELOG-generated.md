## Changelog : opensignauxfaibles (30 derniers jours, au 30 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la qualité des données et la correction de bugs liés à l'intégration des codes NAF. Des ajustements ont été apportés aux tests et aux fichiers de référence pour garantir une meilleure fiabilité des informations affichées et utilisées par la plateforme.

### Évolutions fonctionnelles
- Correction des tests de bout en bout pour les codes NAF, améliorant la précision des données affichées.
- Correction du filtre sur les données d'effectif récentes, qui avait été temporairement désactivé.

### Évolutions techniques
- Amélioration de la génération des fichiers de référence (golden files) avec Go pour une meilleure reproductibilité.
- Correction de plusieurs erreurs dans les migrations de la base de données, notamment des noms incorrects et des références erronées.
- Suppression d'une fonction inutile et d'une migration mal nommée, simplifiant le code.
- Correction de l'utilisation incorrecte du champ "action procol" au lieu de "stade procol" pour le filtrage.
- Ajout du binaire `opensignauxfaibles` au fichier `.gitignore` pour éviter son commit accidentel.

### Autres changements
- Ajout d'un paramètre de schéma à une branche (fusionnée via [#10eee19](https://github.com/signaux-faibles/opensignauxfaibles/pull/10eee19)).
- Mise à jour des fichiers de référence (golden files) suite à l'ajout de nouvelles colonnes NAF.
- Correction du fichier de référence de la CLI.
- Correction du numéro de migration pour les données "procol at date".
