## Changelog : ecobalyse (30 derniers jours)

### Résumé
Les dernières mises à jour d'Ecobalyse apportent des améliorations à l'expérience utilisateur, notamment en facilitant la navigation et la recherche, ainsi que de nouvelles fonctionnalités pour l'analyse de données textiles et l'exportation de favoris. Des corrections de bugs et des optimisations techniques ont également été réalisées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'un autofocus sur le champ de recherche lors de l'ouverture de certaines boîtes modales (#1824).
- Correction d'un message de bannière erroné (#1822).
- Ajout d'une bannière d'avertissement lorsque les conditions d'utilisation ne sont pas acceptées (#1817).
- Possibilité d'exprimer la masse d'un vêtement textile en grammes (#1818).
- Ajout de la possibilité d'exporter et d'importer des favoris (#1784).
- Affichage des ECS (émissions de gaz à effet de serre) pour les invités dans l'explorateur de processus (#1748).
- Introduction de la masse unitaire pour les emballages (#1718).
- Ajout de compléments pour la forêt dans les calculs d'impact (#1750).

### Évolutions techniques
- Suppression du code de l'ancienne version (#1792).
- Correction d'un problème de chargement des processus en production (#1786).
- Suppression des actions de création de release (#1783).
- Refactorisation du code pour utiliser "stage" au lieu de "step" (#1738).
- Suppression du versioning du frontend (#1743).
- Mise à jour des dépendances Python (#1713).
- Mise à jour des dépendances npm (#1775).
- Mise à jour de la librairie litestar de la version 2.19.0 à la 2.20.0 (#1780).

### Autres changements
- Ajout d'une politique de confidentialité en Markdown (#1747).
- Modification de l'accord de conditions d'utilisation (#1627).
- Documentation : l'API n'est plus versionnée (#1742).
- Ajout de nouveaux ingrédients pour les données (#1670).
- Correction d'un problème de pâturage permanent (#1793).
- Correction d'un bug lié à l'application de `massperunit` aux emballages (#1763).
- Correction d'un bug de perte de données de session lors de la navigation entre différentes versions (#1756).
- Ajout d'un slash manquant au code v7 pour les textiles (#1777).
- Modification de l'affichage du nom "Proxy" pour les emballages (#1711).
