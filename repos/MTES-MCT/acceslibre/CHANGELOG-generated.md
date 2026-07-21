## Changelog : acceslibre (30 derniers jours, au 16 juillet 2026)

### Résumé
Les dernières mises à jour d'acceslibre se concentrent sur l'amélioration de la gestion des ERP labellisés RPA (Référentiel Public d'Accessibilité), avec notamment des ajustements de l'interface utilisateur pour la prise en charge de ce label, des corrections de flux et des restrictions d'édition. Des améliorations de la traduction et de la gestion des dates ont également été apportées. Enfin, plusieurs dépendances ont été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles

- Ajout de la gestion du label RPA : les ERP labellisés RPA ne peuvent plus être modifiés. [#2698](https://github.com/MTES-MCT/acceslibre/issues/2698) et [#2691](https://github.com/MTES-MCT/acceslibre/issues/2691)
- Amélioration de l'affichage et du fonctionnement du bouton de traduction. [#2726](https://github.com/MTES-MCT/acceslibre/issues/2726)
- Correction de l'affichage du badge RPA et de la logique d'affichage de la page de réclamation. [#2715](https://github.com/MTES-MCT/acceslibre/issues/2715) et [#2714](https://github.com/MTES-MCT/acceslibre/issues/2714)
- Amélioration du flux de réclamation avec des mises à jour de la page de succès et des conditions d'accès. [#2713](https://github.com/MTES-MCT/acceslibre/issues/2713), [#2701](https://github.com/MTES-MCT/acceslibre/issues/2701), [#2700](https://github.com/MTES-MCT/acceslibre/issues/2700)
- Modification du libellé et du positionnement du registre d'accessibilité pour les ERP RPA. [#2711](https://github.com/MTES-MCT/acceslibre/issues/2711)
- La date de vérification de la mise à jour est maintenant modifiée lors de l'édition, de la création ou de l'importation d'un ERP. [#2712](https://github.com/MTES-MCT/acceslibre/issues/2712)
- Traduction du champ d'accessibilité à la demande. [#2692](https://github.com/MTES-MCT/acceslibre/issues/2692)

### Évolutions techniques

- Mise à jour de Django (minor upgrade). [#2716](https://github.com/MTES-MCT/acceslibre/issues/2716)
- Ajout de la surveillance du cache dans Sentry pour une meilleure détection des problèmes. [#2727](https://github.com/MTES-MCT/acceslibre/issues/2727)
- Modification de la configuration Docker pour mapper le port 8000 du conteneur sur le port 7000 de l'hôte. [#2728](https://github.com/MTES-MCT/acceslibre/issues/2728)

### Autres changements

- Mise à jour de plusieurs dépendances : `eslint`, `prettier`, `djlint`, `django-debug-toolbar`, `psycopg2-binary`, `django-reversion`, `setuptools`, `phonenumbers`, `ruff`, `pnpm`, `dompurify`, `sentry-sdk`, `scrapfly-sdk`, `actions/checkout`, `weasyprint`, `djangorestframework-gis`.
- Suppression des instructions `print` inutiles. [#2694](https://github.com/MTES-MCT/acceslibre/issues/2694)
- Export du flag RPA. [#2601](https://github.com/MTES-MCT/acceslibre/issues/2601) et [#92311ea](https://github.com/MTES-MCT/acceslibre/commit/92311ea76757c97395383f4148286179f966445f)
