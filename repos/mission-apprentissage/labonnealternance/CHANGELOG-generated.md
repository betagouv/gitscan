## Changelog : labonnealternance (30 derniers jours, au 2026-04-16)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment sur la recherche d'alternances, la gestion des offres et l'intégration de nouvelles sources de données. Des corrections de bugs et des optimisations de performance ont également été apportées pour une meilleure stabilité et réactivité de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un lien vers LinkedIn pour la DGEFP [#2842](https://github.com/mission-apprentissage/labonnealternance/issues/2842).
- Amélioration de l'affichage du nombre de candidatures, visible uniquement en cas d'utilisation de la fonction "Smart Apply" [#2848](https://github.com/mission-apprentissage/labonnealternance/issues/2848).
- Mise à jour de la page d'accueil pour les candidats avec une nouvelle présentation "1J1S" [#2834](https://github.com/mission-apprentissage/labonnealternance/issues/2834).
- Correction d'un bug empêchant la création d'entreprises au lieu de CFA [#2803](https://github.com/mission-apprentissage/labonnealternance/issues/2803).
- Amélioration du compteur de candidatures dans les résultats de recherche [#2847](https://github.com/mission-apprentissage/labonnealternance/issues/2847).
- Ajout du tracking Matomo sur la page de simulation [#2832](https://github.com/mission-apprentissage/labonnealternance/issues/2832).
- Ajout de filtres par type de candidature (tags) dans la recherche [#2815](https://github.com/mission-apprentissage/labonnealternance/issues/2815).
- Ajout d'un bloc salaires sur les pages SEO métiers et redirection vers le simulateur de rémunération [#2785](https://github.com/mission-apprentissage/labonnealternance/issues/2785).
- Suppression de la carte dans les résultats de recherche [#2790](https://github.com/mission-apprentissage/labonnealternance/issues/2790).
- Ajout de liens vers Mon Logement Étudiant [#2793](https://github.com/mission-apprentissage/labonnealternance/issues/2793).
- Modification de l'article sur le handicap [#2816](https://github.com/mission-apprentissage/labonnealternance/issues/2816).
- Ajout du formulaire Tally sur la page de recherche [#2817](https://github.com/mission-apprentissage/labonnealternance/issues/2817).
- Mise à jour du plan du site [#2838](https://github.com/mission-apprentissage/labonnealternance/issues/2838).
- Import des flux offres d'emploi EDF et Enedis [#2819](https://github.com/mission-apprentissage/labonnealternance/issues/2819).
- Ajout d'offres aux pages SEO [#2768](https://github.com/mission-apprentissage/labonnealternance/issues/2768).

### Évolutions techniques
- Correction de bugs et stabilisation des healthchecks du stream processor [#2845](https://github.com/mission-apprentissage/labonnealternance/issues/2845).
- Amélioration des lectures MongoDB sur les secondaires pour la recherche [#2849](https://github.com/mission-apprentissage/labonnealternance/issues/2849).
- Augmentation du revalidate ISR des pages Notion à 24 heures [#2855](https://github.com/mission-apprentissage/labonnealternance/issues/2855).
- Correction de la configuration MongoDB (maxPoolSize et secondary helper) [#2856](https://github.com/mission-apprentissage/labonnealternance/issues/2856).
- Ajout de la gestion du rate limit 429 sur l'API job-étudiant avec retry et throttling proactif [#2831](https://github.com/mission-apprentissage/labonnealternance/issues/2831).
- Correction de bugs et amélioration des core web vitals sur la page d'accueil [#2794](https://github.com/mission-apprentissage/labonnealternance/issues/2794).
- Mise à jour des dépendances pour corriger des CVE critiques (handlebars, fast-xml-parser, basic-ftp) [#2810](https://github.com/mission-apprentissage/labonnealternance/issues/2810).
- Suppression des requêtes N+1 sur l'API /api/traininglinks [#2841](https://github.com/mission-apprentissage/labonnealternance/issues/2841).
- Utilisation d'un type de contrat par défaut lors de l'upsert d'offre privée [#2837](https://github.com/mission-apprentissage/labonnealternance/issues/2837).

### Autres changements
- Corrections SEO : canonical, robots.txt pour l'espace pro, meta description pour le simulateur [#2851](https://github.com/mission-apprentissage/labonnealternance/issues/2851).
- Mise à jour des notes des partenaires [#2839](https://github.com/mission-apprentissage/labonnealternance/issues/2839).
- Mise à jour du formatage de la description des offres Hellowork Buddi [#2843](https://github.com/mission-apprentissage/labonnealternance/issues/2843).
- Correction de bugs et améliorations diverses de l'interface utilisateur (UI) [#2827](https://github.com/mission-apprentissage/labonnealternance/issues/2827), [#2784](https://github.com/mission-apprentissage/labonnealternance/issues/2784).
- Mise à jour de la blacklist des CFA [#2833](https://github.com/mission-apprentissage/labonnealternance/issues/2833).
- Correction de bugs et améliorations de l'interface back-office pour les administrateurs [#2828](https://github.com/mission-apprentissage/labonnealternance/issues/2828).
- Correction de bugs liés à l'affichage des offres et des candidatures [#2800](https://github.com/mission-apprentissage/labonnealternance/issues/2800).
- Correction de bugs liés aux tests impactés par la géolocalisation [#2805](https://github.com/mission-apprentissage/labonnealternance/issues/2805).
- Ajout d'une whitelist IP temporaire pour le stress test [#2852](https://github.com/mission-apprentissage/labonnealternance/issues/2852) puis suppression [#2854](https://github.com/mission-apprentissage/labonnealternance/issues/2854).
- Correction de bugs liés à l'affichage des offres sur les pages SEO [#2798](https://github.com/mission-apprentissage/labonnealternance/issues/2798).
- Correction de bugs liés au nombre de candidatures [#2778](https://github.com/mission-apprentissage/labonnealternance/issues/2778).
- Correction de bugs liés à l'import des flux [#2739](https://github.com/mission-apprentissage/labonnealternance/issues/2739).
- Correction de bugs liés à la classification des offres [#2812](https://github.com/mission-apprentissage/labonnealternance/issues/2812).
- Correction de bugs liés à la gestion des entreprises bloquées [#2821](https://github.com/mission-apprentissage/labonnealternance/issues/2821).
- Correction de bugs liés à la page FAQ [#2823](https://github.com/mission-apprentissage/labonnealternance/issues/2823).
- Correction de bugs liés à l'API de géolocalisation [#2771](https://github.com/mission-apprentissage/labonnealternance/issues/2771).
- Correction de bugs liés à l'import des offres [#2765](https://github.com/mission-apprentissage/labonnealternance/issues/2765).
