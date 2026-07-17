## Changelog : acceslibre (30 derniers jours, au 16 juillet 2026)

### Résumé
Les dernières mises à jour d'acceslibre se concentrent sur l'amélioration de l'expérience utilisateur, notamment autour de la gestion des établissements RPA (Référent Préfectoral d'Accessibilité) et de la gestion des droits. Des corrections et des améliorations ont également été apportées à l'interface utilisateur et à la gestion des données. De nombreuses mises à jour de dépendances ont été intégrées pour assurer la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Amélioration de la gestion des établissements RPA : impossibilité de modifier les ERP labellisés RPA [#2698](https://github.com/MTES-MCT/acceslibre/issues/2698).
- Ajout d'un indicateur visuel pour les établissements RPA sur la page d'accessibilité [#2682](https://github.com/MTES-MCT/acceslibre/issues/2682).
- Amélioration du workflow de réclamation (claim) et de la page de succès associée [#2700](https://github.com/MTES-MCT/acceslibre/issues/2700), [#2713](https://github.com/MTES-MCT/acceslibre/issues/2713), [#2714](https://github.com/MTES-MCT/acceslibre/issues/2714).
- Ajout d'un champ "RPA exemption" uniquement visible pour les gestionnaires [#2701](https://github.com/MTES-MCT/acceslibre/issues/2701).
- Export de l'information "RPA" pour les ERP [#2691](https://github.com/MTES-MCT/acceslibre/issues/2691), [#2601](https://github.com/MTES-MCT/acceslibre/issues/2601).
- Correction de l'affichage du bouton de traduction et du rendu du texte [#2726](https://github.com/MTES-MCT/acceslibre/issues/2726).
- Modification de la date `checked_up_to_date_at` lors de la création, modification ou importation d'un ERP [#2712](https://github.com/MTES-MCT/acceslibre/issues/2712).
- Traduction du champ d'accessibilité à la demande [#2692](https://github.com/MTES-MCT/acceslibre/issues/2692).
- Correction de l'affichage du badge RPA si l'ERP n'est pas RPA [#2715](https://github.com/MTES-MCT/acceslibre/issues/2715).

### Évolutions techniques
- Intégration du monitoring du cache dans Sentry pour une meilleure surveillance des performances [#2727](https://github.com/MTES-MCT/acceslibre/issues/2727).
- Mise à jour de la configuration Docker pour mapper le port 8000 du conteneur sur le port 7000 de l'hôte [#2728](https://github.com/MTES-MCT/acceslibre/issues/2728).
- Mise à jour mineure de Django [#2716](https://github.com/MTES-MCT/acceslibre/issues/2716).
- Utilisation d'une locale `fr_FR` pour Faker afin de générer des données plus pertinentes.
- Synchronisation du calcul du taux de complétion.

### Autres changements
- Mises à jour de nombreuses dépendances (eslint, prettier, djlint, faker, scrapfly-sdk, gunicorn, etc.) pour assurer la sécurité et la stabilité de la plateforme.
- Nettoyage du code (suppression de prints).
