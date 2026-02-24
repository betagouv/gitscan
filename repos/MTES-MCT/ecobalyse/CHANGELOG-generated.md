## Changelog : ecobalyse (30 derniers jours)

### Résumé
Les dernières mises à jour d'ecobalyse apportent des améliorations à l'expérience utilisateur, notamment au niveau des favoris, de l'interface et de la navigation. De nouvelles données ont été ajoutées pour les ingrédients et les compléments forestiers. Des corrections de bugs ont été implémentées pour améliorer la stabilité et la fiabilité de l'application. Enfin, des optimisations techniques et des mises à jour de dépendances ont été réalisées.

### Évolutions fonctionnelles
- Possibilité d'exporter et d'importer les favoris (#1784)
- Amélioration des icônes des favoris (#1823)
- Ajout d'une alerte lorsque les conditions d'utilisation ne sont pas acceptées (#1817)
- Possibilité d'exprimer la masse des vêtements textiles en grammes (#1818)
- Autorisation de soumettre la modification du nom d'un favori en appuyant sur Entrée (#1774)
- Ajout de nouveaux ingrédients dans la base de données (#1670)
- Introduction de la notion de "masse par unité" pour les emballages (#1718)
- Affichage des ECS (émissions de gaz à effet de serre) pour les invités dans l'explorateur de processus (#1748)
- Ajout de compléments forestiers (#1750)

### Évolutions techniques
- Amélioration de l'implémentation de l'autofocus sur les champs de saisie (#1834)
- Suppression de la transition CSS sur les modales d'autocomplétion (#1826)
- Suppression du code lié à l'ancienne version de l'application (#1792)
- Suppression des actions de création de release GitHub (#1783)
- Suppression du versionnement du frontend (#1743)
- Mise à jour de la dépendance `litestar` de la version 2.19.0 à la version 2.20.0 (#1780)
- Mise à jour des dépendances Python (#1713, #1743)
- Suppression du code de versionnement de l'API (#1742)
- Refactorisation pour utiliser "stage" au lieu de "step" dans le code (#1738)

### Autres changements
- Correction d'un message de bannière erroné (#1822)
- Correction d'un bug empêchant la perte de données de session lors de la navigation entre les versions (#1756)
- Correction d'un bug lié à l'affichage des impacts détaillés pour les objets et les VELI (#1709)
- Ajout d'une politique de confidentialité en Markdown (#1747)
- Mise à jour des conditions d'utilisation (#1627)
- Correction d'un bug sur les pâturages permanents (#1793)
- Correction de l'application de la masse par unité aux emballages (#1763)
- Correction d'un problème d'affichage de la légende des graphiques comparatifs lors de l'exportation (#1704)
- Mise à jour des exemples VELI (#1716)
- Mise à jour de la base de données avec des données et l'ajout d'un processus CFF (#1708)
