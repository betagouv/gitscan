## Changelog : labonnealternance (30 derniers jours, au 16 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment sur la recherche d'offres et la gestion des candidatures. Des corrections de bugs ont également été apportées pour stabiliser la plateforme et améliorer sa performance, ainsi que des mises à jour de flux d'offres et de la gestion des partenaires.

### Évolutions fonctionnelles
- Ajout d'un lien vers LinkedIn pour la DGEFP [#2842](https://github.com/mission-apprentissage/labonnealternance/issues/2842).
- Amélioration de l'affichage du nombre de candidatures, visible uniquement en cas d'utilisation de la fonctionnalité "Smart Apply" [#2848](https://github.com/mission-apprentissage/labonnealternance/issues/2848).
- Création d'une nouvelle landing page pour les candidats "1 jour 1 solution" [#2834](https://github.com/mission-apprentissage/labonnealternance/issues/2834).
- Correction d'un bug empêchant la création d'entreprises au lieu de CFA [#2803](https://github.com/mission-apprentissage/labonnealternance/issues/2803).
- Mise à jour du plan du site [#2838](https://github.com/mission-apprentissage/labonnealternance/issues/2838).
- Ajout d'un filtre par type de candidature (tags) [#2815](https://github.com/mission-apprentissage/labonnealternance/issues/2815).
- Ajout d'un bloc salaires sur les pages SEO métiers et redirection vers le simulateur de rémunération [#2785](https://github.com/mission-apprentissage/labonnealternance/issues/2785).
- Suppression de la carte dans les résultats de recherche [#2790](https://github.com/mission-apprentissage/labonnealternance/issues/2790).
- Ajout de rubriques vers Mon Logement Étudiant [#2793](https://github.com/mission-apprentissage/labonnealternance/issues/2793).
- Modification de l'article dédié au handicap [#2816](https://github.com/mission-apprentissage/labonnealternance/issues/2816).
- Ajout du tracking Matomo sur la simulation [#2832](https://github.com/mission-apprentissage/labonnealternance/issues/2832).
- Ajout du formulaire Tally sur la page de recherche [#2817](https://github.com/mission-apprentissage/labonnealternance/issues/2817).
- Import des flux d'offres EDF et Enedis [#2819](https://github.com/mission-apprentissage/labonnealternance/issues/2819).

### Évolutions techniques
- Correction d'un bug lié aux menus déroulants provenant de Notion [#2859](https://github.com/mission-apprentissage/labonnealternance/issues/2859).
- Mise à jour de la configuration MongoDB pour améliorer la performance et la stabilité [#2857](https://github.com/mission-apprentissage/labonnealternance/issues/2857).
- Augmentation du temps de revalidation ISR des pages Notion à 24 heures pour optimiser la mise en cache [#2855](https://github.com/mission-apprentissage/labonnealternance/issues/2855).
- Amélioration de la gestion des healthchecks et réduction de la pression sur le stream processor [#2845](https://github.com/mission-apprentissage/labonnealternance/issues/2845).
- Ajout de lectures MongoDB sur les secondaires pour la recherche [#2849](https://github.com/mission-apprentissage/labonnealternance/issues/2849).
- Correction de la priorité de `human_verification` dans `getClassificationFromLab` [#2836](https://github.com/mission-apprentissage/labonnealternance/issues/2836).
- Ajout de lectures MongoDB sur secondaires pour la recherche [#2849](https://github.com/mission-apprentissage/labonnealternance/issues/2849).
- Stabilisation des healthchecks et réduction de la pression du stream processor [#2845](https://github.com/mission-apprentissage/labonnealternance/issues/2845).
- Correction de bugs et amélioration des Core Web Vitals sur la page d'accueil [#2814](https://github.com/mission-apprentissage/labonnealternance/issues/2814).
- Correction de vulnérabilités critiques dans les dépendances (handlebars, fast-xml-parser, basic-ftp) [#2810](https://github.com/mission-apprentissage/labonnealternance/issues/2810).
- Gestion du rate limit 429 sur l'API job-étudiant avec retry et throttling proactif [#2831](https://github.com/mission-apprentissage/labonnealternance/issues/2831).
- Élimination des requêtes N+1 sur l'API `/api/traininglinks` [#2841](https://github.com/mission-apprentissage/labonnealternance/issues/2841).
- Utilisation d'un type de contrat par défaut lors de l'upsert d'offre privée [#2837](https://github.com/mission-apprentissage/labonnealternance/issues/2837).

### Autres changements
- Corrections SEO : ajout de balises canonical, configuration du robots.txt pour l'espace pro, et meta descriptions pour le simulateur [#2851](https://github.com/mission-apprentissage/labonnealternance/issues/2851).
- Mise à jour des notes des partenaires [#2839](https://github.com/mission-apprentissage/labonnealternance/issues/2839).
- Mise à jour des astuces et du plan du site [#2830](https://github.com/mission-apprentissage/labonnealternance/issues/2830).
- Correction d'un lien vers le Grand Est [#2835](https://github.com/mission-apprentissage/labonnealternance/issues/2835).
- Ajout d'une whitelist IP temporaire pour le stress test (puis suppression) [#2852](https://github.com/mission-apprentissage/labonnealternance/issues/2852), [#2854](https://github.com/mission-apprentissage/labonnealternance/issues/2854).
- Correction du formatage de la description des offres Hellowork Buddi [#2843](https://github.com/mission-apprentissage/labonnealternance/issues/2843).
- Ajout d'une whitelist pour la classification des CFA [#2764](https://github.com/mission-apprentissage/labonnealternance/issues/2764).
- Amélioration de la gestion des erreurs lors du parsing de la géolocalisation [#2771](https://github.com/mission-apprentissage/labonnealternance/issues/2771).
- Correction d'une erreur liée à l'object ID [#2776](https://github.com/mission-apprentissage/labonnealternance/issues/2776).
- Ajout d'un script pour analyser la blocklist des CFA [#2822](https://github.com/mission-apprentissage/labonnealternance/issues/2822).
- Correction de bugs et amélioration de l'interface utilisateur de l'espace CFA/entreprises partenaires [#2784](https://github.com/mission-apprentissage/labonnealternance/issues/2784).
- Ajout de la récurrence du rommage des offres [#2802](https://github.com/mission-apprentissage/labonnealternance/issues/2802).
- Correction de bugs Sentry sur l'interface utilisateur [#2807](https://github.com/mission-apprentissage/labonnealternance/issues/2807).
- Mise à jour du flux Hellowork Buddi [#2763](https://github.com/mission-apprentissage/labonnealternance/issues/2763).
- Correction des tests impactés par la géolocalisation [#2805](https://github.com/mission-apprentissage/labonnealternance/issues/2805).
