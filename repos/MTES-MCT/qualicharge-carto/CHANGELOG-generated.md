## Changelog : qualicharge-carto (30 derniers jours, au 18 juillet 2026)

### Résumé
Les dernières mises à jour de qualicharge-carto se concentrent sur l'enrichissement des données tarifaires des bornes de recharge, l'amélioration de l'interface utilisateur et la correction de bugs pour une meilleure expérience utilisateur. De nouveaux opérateurs (BP, R3, Driveco, Total, Izivia, Milence, Monta, Plenitude, Shell) ont été ajoutés et les tarifs ont été mis à jour.

### Évolutions fonctionnelles
- Ajout des tarifs des bornes de recharge EVzen [#f58ff52](https://github.com/MTES-MCT/qualicharge-carto/commit/f58ff52).
- Ajout des tarifs de Milence, Monta, Plenitude et Shell [#33ccae2](https://github.com/MTES-MCT/qualicharge-carto/commit/33ccae2).
- Ajout des opérateurs BP, R3 et Driveco avec actualisation de la liste des points de charge [#4cf3132](https://github.com/MTES-MCT/qualicharge-carto/commit/4cf3132), [#63cef03](https://github.com/MTES-MCT/qualicharge-carto/commit/63cef03), [#71316c5](https://github.com/MTES-MCT/qualicharge-carto/commit/71316c5).
- Ajout des tarifs de Total et Izivia [#65c1673](https://github.com/MTES-MCT/qualicharge-carto/commit/65c1673).
- Possibilité de masquer les modales [#ce0bd7a](https://github.com/MTES-MCT/qualicharge-carto/commit/ce0bd7a).
- Affichage de la fraîcheur des données dynamiques [#9e3f7c7](https://github.com/MTES-MCT/qualicharge-carto/commit/9e3f7c7).
- Restriction de la carte aux stations actives [#eb044e6](https://github.com/MTES-MCT/qualicharge-carto/commit/eb044e6).
- Superposition des stations les plus récentes [#ad679f3](https://github.com/MTES-MCT/qualicharge-carto/commit/ad679f3).

### Évolutions techniques
- Regroupement des tarifs par point de charge pour une meilleure gestion [#6b350d4](https://github.com/MTES-MCT/qualicharge-carto/commit/6b350d4).
- Amélioration de l'ancrage des marqueurs sur la carte [#f08659b](https://github.com/MTES-MCT/qualicharge-carto/commit/f08659b).
- Regroupement davantage des stations sur la carte pour une meilleure performance [#1126471](https://github.com/MTES-MCT/qualicharge-carto/commit/1126471).
- Ajustement du positionnement de la barre d'outils de la carte et des contrôles de zoom pour une meilleure réactivité [#392af95](https://github.com/MTES-MCT/qualicharge-carto/commit/392af95).
- Capture des changements d'URL hash pour une meilleure gestion de l'état de l'application [#5ebf435](https://github.com/MTES-MCT/qualicharge-carto/commit/5ebf435).

### Autres changements
- Correction de l'affichage de l'état du point de charge sans statut de prise [#8f6e0d3](https://github.com/MTES-MCT/qualicharge-carto/commit/8f6e0d3).
- Exclusion des statuts périmés des compteurs en temps réel [#7321de8](https://github.com/MTES-MCT/qualicharge-carto/commit/7321de8).
- Masquage des restrictions tarifaires valables tous les jours [#2bea658](https://github.com/MTES-MCT/qualicharge-carto/commit/2bea658).
- Simplification du titre des tarifs multi-PDC [#1be5c71](https://github.com/MTES-MCT/qualicharge-carto/commit/1be5c71).
- Contextualisation des tarifs par point de charge [#43c350c](https://github.com/MTES-MCT/qualicharge-carto/commit/43c350c).
- Modification du badge de puissance max pour une meilleure lisibilité [#a19a80a](https://github.com/MTES-MCT/qualicharge-carto/commit/a19a80a).
- Mise à jour du texte des modales et alignement de la logique de rendu du texte [#5370baa](https://github.com/MTES-MCT/qualicharge-carto/commit/5370baa).
