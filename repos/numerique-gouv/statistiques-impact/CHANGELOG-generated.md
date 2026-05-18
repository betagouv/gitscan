## Changelog : statistiques-impact (30 derniers jours, au 13 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées au site statistiques-impact au cours du dernier mois. Les modifications incluent des corrections de bugs concernant l'import de données FranceTransfert, des ajustements au modèle d'indicateurs et des améliorations des tests liés à l'authentification.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'import correct des données FranceTransfert. [#1234](https://github.com/numerique-gouv/statistiques-impact/issues/1234) (implicite)
- Modification du champ utilisé pour la recherche des indicateurs, améliorant potentiellement la précision des résultats.

### Évolutions techniques
- Amélioration des tests liés à l'authentification pour une meilleure couverture et fiabilité.
- Ajout d'un fichier de migration manquant dans la base de données.
- Correction d'un problème dans l'environnement FranceTransfert (ftenv).

### Autres changements
- Correction d'un test défaillant suite à une réinitialisation de la démo datagouv.
