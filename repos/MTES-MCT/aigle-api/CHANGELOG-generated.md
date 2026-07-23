## Changelog : aigle-api (30 derniers jours, au 21 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des données, notamment concernant l'importation et la mise à jour des détections et des zones personnalisées. Des corrections ont également été apportées au flux de prescription et à l'affectation des détections aux tuiles. Enfin, des outils internes pour le suivi et l'analyse des données DDTM ont été ajoutés.

### Évolutions fonctionnelles
- Ajout de la possibilité de bloquer les zones urbaines [#1d54d99](https://github.com/MTES-MCT/aigle-api/commit/1d54d99).
- Amélioration du tableau de bord DDT [#7e91360](https://github.com/MTES-MCT/aigle-api/commit/7e91360).
- Correction du flux de prescription [#85bb189](https://github.com/MTES-MCT/aigle-api/commit/85bb189).
- Correction de l'affectation des détections aux bons ensembles de tuiles [#042df3c](https://github.com/MTES-MCT/aigle-api/commit/042df3c).
- Ajout d'une interface de statistiques pour DDTM (usage interne uniquement) [#08eefb2](https://github.com/MTES-MCT/aigle-api/commit/08eefb2).

### Évolutions techniques
- Optimisation des performances de la commande `update_detectionobject_commune` [#8ea8e12](https://github.com/MTES-MCT/aigle-api/commit/8ea8e12).
- Ajout d'un paramètre `force` à la commande `update_detectionobject_commune` [#df1f6cc](https://github.com/MTES-MCT/aigle-api/commit/df1f6cc).
- Amélioration de la logique de liaison entre les détections et les zones géographiques personnalisées [#4233832](https://github.com/MTES-MCT/aigle-api/commit/4233832).
- Amélioration de la gestion des utilisateurs et des groupes lors du déploiement [#89ef479](https://github.com/MTES-MCT/aigle-api/commit/89ef479).
- Amélioration des commandes `sitadel` et `import_sitadel` [#c1bb813](https://github.com/MTES-MCT/aigle-api/commit/c1bb813) et [#fd88789](https://github.com/MTES-MCT/aigle-api/commit/fd88789).
- Amélioration des commandes d'importation de données (parcelles, détections) [#28faa90](https://github.com/MTES-MCT/aigle-api/commit/28faa90) et [#25bd268](https://github.com/MTES-MCT/aigle-api/commit/25bd268).
- Amélioration de la stratégie de déploiement de Celery [#84a93f7](https://github.com/MTES-MCT/aigle-api/commit/84a93f7).
- Mise en place d'améliorations de sécurité [#542f582](https://github.com/MTES-MCT/aigle-api/commit/542f582).
- Pruning des détections situées en dehors des zones personnalisées [#9048018](https://github.com/MTES-MCT/aigle-api/commit/9048018).

### Autres changements
- Nettoyage et simplification de la commande `import_detections` [#aff8f3e](https://github.com/MTES-MCT/aigle-api/commit/aff8f3e).
- Suppression des routes liées aux statistiques [#b967c85](https://github.com/MTES-MCT/aigle-api/commit/b967c85).
- Correction de l'actualisation du cache après les commandes d'importation [#fcc747d](https://github.com/MTES-MCT/aigle-api/commit/fcc747d).
- Déploiement simplifié avec la possibilité de déployer une seule batch ou une seule ZAE [#987b470](https://github.com/MTES-MCT/aigle-api/commit/987b470).
- Amélioration du déploiement ciblé (parties spécifiques) [#5842fe5](https://github.com/MTES-MCT/aigle-api/commit/5842fe5).
- Ajout de la possibilité de déployer en un clic [#d0adc04](https://github.com/MTES-MCT/aigle-api/commit/d0adc04).
- Safeguard pour la création des détections [#d0f54d4](https://github.com/MTES-MCT/aigle-api/commit/d0f54d4).
