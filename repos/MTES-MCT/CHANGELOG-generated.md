# Synthèse d'activité : MTES-MCT (du 01/09 au 04/10)

## Résumé de l'activité
L'activité de l'organisation a été marquée par une volonté de moderniser l'expérience utilisateur et de renforcer la fiabilité des données à travers de nombreux services. Les efforts se sont concentrés sur la refonte d'interfaces pour les rendre plus intuitives (notamment pour [otelo](/repos/MTES-MCT/otelo) et [sparte](/repos/MTES-MCT/sparte)) et sur l'amélioration de l'accessibilité numérique (RGAA) pour des outils comme [vigieau](/repos/MTES-MCT/vigieau) et [zero-logement-vacant](/repos/MTES-MCT/zero-logement-vacant).

L'automatisation est également un moteur majeur de cette période, avec l'introduction de l'autovalidation des dossiers pour [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) et une gestion plus fluide des bordereaux pour [trackdechets](/repos/MTES-MCT/trackdechets). Ces évolutions visent à réduire la charge administrative des utilisateurs tout en garantissant une meilleure précision des indicateurs environnementaux et de logement.

## Sécurité
- **Renforcement de l'authentification** : Déploiement de l'authentification à deux facteurs (2FA) sur plusieurs plateformes pour sécuriser les accès : [otelo](/repos/MTES-MCT/otelo), [oilhi-cms](/repos/MTES-MCT/oilhi-cms), [zero-logement-vacant-site-vitrine](/repos/MTES-MCT/zero-logement-vacant-site-vitrine) et [mobilic-metabase](/repos/MTES-MCT/mobilic-metabase).
- **Correction de vulnérabilités** :
    - Protection contre les injections SQL [resorption-bidonvilles](/repos/MTES-MCT/resorption-bidonvilles) et les attaques par déni de service (DoS) [mobilic-api](/repos/MTES-MCT/mobilic-api).
    - Correction de failles de type SSRF [trackdechets](/repos/MTES-MCT/trackdechets) et de vulnérabilités BOLA permettant des fuites de données [mobilic-api](/repos/MTES-MCT/mobilic-api).
    - Résolution de vulnérabilités dans les dépendances [vigieau](/repos/MTES-MCT/vigieau) et [qualicharge](/repos/MTES-MCT/qualicharge).
- **Protection des données** : Amélioration de la confidentialité des données personnelles et de l'anonymisation [trackdechets](/repos/MTES-MCT/trackdechets) et [mobilic-api](/repos/MTES-MCT/mobilic-api).

## Autres changements notables
- **Migrations technologiques majeures** :
    - Passage à Inertia 3 et Maplibre 6 pour [vizeau](/repos/MTES-MCT/vizeau).
    - Mise à jour vers React 18 pour [partaj](/repos/MTES-MCT/partaj) et React Router 8 pour [rapportnav2](/repos/MTES-MCT/rapportnav2).
    - Montée de version globale vers R 4.6.0 pour l'ensemble des modules du [parcours-r](/repos/MTES-MCT/parcours-r).
- **Évolutions d'infrastructure** :
    - Migration du stockage de fichiers vers un système S3 pour [envergo](/repos/MTES-MCT/envergo).
    - Mise en place de déploiements automatisés sur Scaleway pour [prelevements-deau-web](/repos/MTES-MCT/prelevements-deau-web).
    - Automatisation des builds Android via EAS pour [monitor-field](/repos/MTES-MCT/monitor-field).

## Dépôts les plus actifs
- [otelo](/repos/MTES-MCT/otelo) : Refonte de l'expérience de simulation, ajout de tutoriels et renforcement de la sécurité.
- [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend) : Mise en place de l'autovalidation des dossiers et amélioration de l'analyse documentaire par IA.
- [ecobalyse](/repos/MTES-MCT/ecobalyse) : Enrichissement massif de la base de données et introduction d'une nouvelle API.
- [trackdechets](/repos/MTES-MCT/trackdechets) : Amélioration de l'interface mobile et sécurisation des processus de bordereaux.
- [partageonsleau-orchestration](/repos/MTES-MCT/partageonsleau-orchestration) : Optimisation de l'ingestion et du traitement de données multi-sources.
