## Changelog : acceslibre (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la collecte de données d'accessibilité, notamment avec l'ajout de nouvelles questions signalétiques et l'intégration de données APIDAE. Des corrections et améliorations ont également été apportées à l'interface utilisateur et à l'administration du site, ainsi qu'à la gestion des PDF et des exports.

### Évolutions fonctionnelles
- Ajout de nouvelles questions signalétiques pour une collecte d'informations plus précise sur l'accessibilité des établissements ([#2620](https://github.com/MTES-MCT/acceslibre/issues/2620)).
- Intégration des données APIDAE pour enrichir les informations sur les établissements ([#2641](https://github.com/MTES-MCT/acceslibre/issues/2641)).
- Possibilité d'exporter les informations des mails ([#2652](https://github.com/MTES-MCT/acceslibre/issues/2652)).
- Amélioration du lien vers acceslibre dans les widgets, avec ouverture dans un nouvel onglet ([#2654](https://github.com/MTES-MCT/acceslibre/issues/2654)).
- Correction de l'affichage du taux de complétion, en excluant certaines questions ([#2653](https://github.com/MTES-MCT/acceslibre/issues/2653), [#2656](https://github.com/MTES-MCT/acceslibre/issues/2656)).
- Restriction de l'accès à l'interface d'administration aux utilisateurs disposant des droits nécessaires ([#2652](https://github.com/MTES-MCT/acceslibre/issues/2652)).
- Possibilité de contourner les vérifications de doublons ([#2626](https://github.com/MTES-MCT/acceslibre/issues/2626)).
- Utilisation de POST pour la génération des PDF RPA ([#2623](https://github.com/MTES-MCT/acceslibre/issues/2623)).

### Évolutions techniques
- Mise à jour de Django ([#2625](https://github.com/MTES-MCT/acceslibre/issues/2625)).
- Utilisation de Redis pour stocker les événements des widgets et les vider dans la base de données toutes les heures ([#2624](https://github.com/MTES-MCT/acceslibre/issues/2624)).
- Optimisation de la pagination en mettant en cache le nombre d'éléments par requête ([#2621](https://github.com/MTES-MCT/acceslibre/issues/2621)).
- Amélioration de la sélection des données de la commune pour optimiser les requêtes ([#2655](https://github.com/MTES-MCT/acceslibre/issues/2655)).
- Suppression temporaire de la génération de PDF RPA en raison de problèmes ([#2622](https://github.com/MTES-MCT/acceslibre/issues/2622), [#2611](https://github.com/MTES-MCT/acceslibre/issues/2611)).

### Autres changements
- Correction de la version des paquets pour assurer la cohérence de l'environnement ([#2635](https://github.com/MTES-MCT/acceslibre/issues/2635)).
- Mise à jour de la configuration pour désactiver temporairement l'acquisition Scrapfly en attendant une réécriture ([#2640](https://github.com/MTES-MCT/acceslibre/issues/2640)).
- Ajout d'une contrainte de connexion pour l'assistant de contribution ([#2636](https://github.com/MTES-MCT/acceslibre/issues/2636)).
- Diverses mises à jour de dépendances (Sentry, dompurify, eslint, pandas, ipython, requests, gunicorn, ruff, psycopg2, frictionless, django-modeltranslation, pnpm).
