## Changelog : labonnealternance (30 derniers jours, au 2026-04-21)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment l'intégration de candidatures directes vers Taleez et l'amélioration du processus de candidature spontanée. Des corrections de bugs et des optimisations de performance ont également été apportées pour améliorer la stabilité et la réactivité de la plateforme. Enfin, des flux d'import d'offres ont été mis à jour et de nouvelles sources ont été intégrées.

### Évolutions fonctionnelles
- Intégration de candidatures directes vers Taleez, incluant l'affichage correct de la modale de candidature sur Taleez [#2804](https://github.com/mission-apprentissage/labonnealternance/issues/2804) et [#2865](https://github.com/mission-apprentissage/labonnealternance/issues/2865).
- Amélioration du processus de candidature spontanée avec l'ajout de tags et la refonte de l'interface [#2787](https://github.com/mission-apprentissage/labonnealternance/issues/2787).
- Ajout d'un bouton "Je postule" fonctionnel sur les offres [#2850](https://github.com/mission-apprentissage/labonnealternance/issues/2850).
- Ajout d'un tracking Matomo sur la simulation de rémunération [#2832](https://github.com/mission-apprentissage/labonnealternance/issues/2832).
- Ajout d'un lien vers LinkedIn DGEFP [#2842](https://github.com/mission-apprentissage/labonnealternance/issues/2842).
- Ajout de la possibilité de filtrer les offres par type de candidature (tags) [#2815](https://github.com/mission-apprentissage/labonnealternance/issues/2815).
- Ajout de blocs salaires sur les pages SEO métiers [#2785](https://github.com/mission-apprentissage/labonnealternance/issues/2785).
- Ajout d'un formulaire Tally sur la recherche [#2817](https://github.com/mission-apprentissage/labonnealternance/issues/2817).
- Ajout d'une landing page pour la campagne "1 jour 1 solution" [#2834](https://github.com/mission-apprentissage/labonnealternance/issues/2834).
- Import des flux offres d'EDF et d'Enedis [#2819](https://github.com/mission-apprentissage/labonnealternance/issues/2819).
- Ajout de la possibilité de whitelister les offres de GEIQ et de CFA d'entreprise [#2840](https://github.com/mission-apprentissage/labonnealternance/issues/2840).
- Ajout d'un bloc "Mes Aides" [#2793](https://github.com/mission-apprentissage/labonnealternance/issues/2793).
- Mise à jour du texte et des images de la RCO [#2860](https://github.com/mission-apprentissage/labonnealternance/issues/2860).

### Évolutions techniques
- Correction d'un job de resynchronisation des statistiques LBA [#2846](https://github.com/mission-apprentissage/labonnealternance/issues/2846).
- Optimisation des requêtes pour éviter les problèmes de N+1 sur l'API training links [#2841](https://github.com/mission-apprentissage/labonnealternance/issues/2841).
- Amélioration de la gestion du rate limit de l'API job-étudiant avec retry et throttling proactif [#2831](https://github.com/mission-apprentissage/labonnealternance/issues/2831).
- Correction de bugs et amélioration des Core Web Vitals sur la page d'accueil [#2794](https://github.com/mission-apprentissage/labonnealternance/issues/2794).
- Correction de CVE critiques dans les dépendances (handlebars, fast-xml-parser, basic-ftp) [#2810](https://github.com/mission-apprentissage/labonnealternance/issues/2810).
- Ajout de lectures MongoDB sur les secondaires pour la recherche [#2849](https://github.com/mission-apprentissage/labonnealternance/issues/2849).
- Amélioration de la stabilité des healthchecks et réduction de la pression du stream processor [#2845](https://github.com/mission-apprentissage/labonnealternance/issues/2845).
- Correction de bugs et amélioration des performances de Metabase.
- Mise à jour de la configuration MongoDB pour améliorer la performance et la stabilité.
- Correction de bugs liés à l'affichage des menus déroulants provenant de Notion [#2859](https://github.com/mission-apprentissage/labonnealternance/issues/2859).
- Correction d'un bug empêchant l'affichage correct du nombre de candidatures en cas de "smart apply" [#2848](https://github.com/mission-apprentissage/labonnealternance/issues/2848).

### Autres changements
- Correction du fichier robots.txt [#2852](https://github.com/mission-apprentissage/labonnealternance/issues/2852).
- Mise à jour du plan du site [#2838](https://github.com/mission-apprentissage/labonnealternance/issues/2838).
- Corrections SEO (canonical, meta descriptions, sitemap) [#2851](https://github.com/mission-apprentissage/labonnealternance/issues/2851) et [#2809](https://github.com/mission-apprentissage/labonnealternance/issues/2809).
- Mise à jour des notes des partenaires [#2839](https://github.com/mission-apprentissage/labonnealternance/issues/2839).
- Correction de l'envoi des emails RDV [#2808](https://github.com/mission-apprentissage/labonnealternance/issues/2808).
- Correction de l'affichage des offres sur l'espace CFA/entreprises partenaires [#2784](https://github.com/mission-apprentissage/labonnealternance/issues/2784).
- Correction du formatage de la description des offres Hellowork Buddi [#2739](https://github.com/mission-apprentissage/labonnealternance/issues/2739).
- Correction d'une erreur Object ID [#2776](https://github.com/mission-apprentissage/labonnealternance/issues/2776).
- Mise à jour de l'article handicap [#2816](https://github.com/mission-apprentissage/labonnealternance/issues/2816).
- Correction de la page FAQ [#2823](https://github.com/mission-apprentissage/labonnealternance/issues/2823).
- Correction de l'affichage des liens de recherche [#2853](https://github.com/mission-apprentissage/labonnealternance/issues/2853).
- Correction de la création d'entreprise au lieu de CFA [#2803](https://github.com/mission-apprentissage/labonnealternance/issues/2803).
- Correction du compteur de candidatures dans les résultats de recherche [#2847](https://github.com/mission-apprentissage/labonnealternance/issues/2847).
- Augmentation du revalidate ISR des pages Notion [#2855](https://github.com/mission-apprentissage/labonnealternance/issues/2855).
- Correction de bugs dans le back-office pour les administrateurs LBA [#2828](https://github.com/mission-apprentissage/labonnealternance/issues/2828).
- Correction de bugs liés aux flux Kelio, Laposte et Leboncoin [#2827](https://github.com/mission-apprentissage/labonnealternance/issues/2827).
- Ajout d'un script d'analyse de la blocklist CFA [#2822](https://github.com/mission-apprentissage/labonnealternance/issues/2822).
- Masquage des candidatures recruteur LBA sans email [#2826](https://github.com/mission-apprentissage/labonnealternance/issues/2826).
- Correction de bugs liés à l'import des offres [#2763](https://github.com/mission-apprentissage/labonnealternance/issues/2763).
- Correction de bugs liés à l'API Geoloc [#2771](https://github.com/mission-apprentissage/labonnealternance/issues/2771).
- Correction de bugs liés à l'export Cegid [#2739](https://github.com/mission-apprentissage/labonnealternance/issues/2739).
- Correction de la blacklist CFA [#2833](https://github.com/mission-apprentissage/labonnealternance/issues/2833).
- Correction de l'affichage des liens vers le Grand Est [#2835](https://github.com/mission-apprentissage/labonnealternance/issues/2835).
