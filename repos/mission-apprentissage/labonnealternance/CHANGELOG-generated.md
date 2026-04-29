## Changelog : labonnealternance (30 derniers jours, au 2026-04-28)

### Résumé
Les dernières mises à jour de la plateforme La Bonne Alternance se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de nouvelles pages SEO pour les villes, l'optimisation de la recherche d'offres et l'intégration de nouveaux flux d'offres d'apprentissage. Des corrections de bugs et des améliorations techniques ont également été apportées pour stabiliser la plateforme et améliorer ses performances.

### Évolutions fonctionnelles
- Ajout du tracking Matomo pour les parcours utilisateurs clés (recherche, découverte, candidature) [#2871](https://github.com/mission-apprentissage/labonnealternance/issues/2871).
- Ajout de 10 nouvelles pages ville optimisées pour le SEO [#2872](https://github.com/mission-apprentissage/labonnealternance/issues/2872).
- Exclusion des offres des entreprises partenaires reçues directement, pour une meilleure gestion des sources [#2813](https://github.com/mission-apprentissage/labonnealternance/issues/2813).
- Amélioration de la navigation sur la page de résultats de recherche [#2861](https://github.com/mission-apprentissage/labonnealternance/issues/2861).
- Possibilité de postuler à des offres sans adresse email, en utilisant uniquement un numéro de téléphone [#2863](https://github.com/mission-apprentissage/labonnealternance/issues/2863).
- Ajout de la clé API Taleez pour l'intégration avec cette plateforme [#2873](https://github.com/mission-apprentissage/labonnealternance/issues/2873).
- Correction de l'affichage du nombre de candidatures pour les offres partenaires [#2867](https://github.com/mission-apprentissage/labonnealternance/issues/2867).
- Amélioration de l'interface modale pour les candidatures externes sur Taleez [#2870](https://github.com/mission-apprentissage/labonnealternance/issues/2870).
- Correction du CTA "Je postule" sur les offres [#2850](https://github.com/mission-apprentissage/labonnealternance/issues/2850).
- Ajout de 8 nouvelles pages ville optimisées pour le SEO [#2875](https://github.com/mission-apprentissage/labonnealternance/issues/2875).
- Correction du scroll vers la première candidature spontanée [#2874](https://github.com/mission-apprentissage/labonnealternance/issues/2874).
- Ajout d'une landing page pour la campagne "1 jour 1 stagiaire" [#2834](https://github.com/mission-apprentissage/labonnealternance/issues/2834).
- Ajout de blocs salaires sur les pages SEO métiers et redirection vers le simulateur de rémunération [#2785](https://github.com/mission-apprentissage/labonnealternance/issues/2785).
- Ajout de liens vers Mon Logement Étudiant [#2793](https://github.com/mission-apprentissage/labonnealternance/issues/2793).
- Ajout de flux import pour EDF et Enedis [#2819](https://github.com/mission-apprentissage/labonnealternance/issues/2819).
- Ajout d'un formulaire Tally sur la page de recherche [#2817](https://github.com/mission-apprentissage/labonnealternance/issues/2817).
- Ajout d'un bloc "Mes Aides" [#2816](https://github.com/mission-apprentissage/labonnealternance/issues/2816).
- Ajout de filtres par type de candidature (tags) [#2815](https://github.com/mission-apprentissage/labonnealternance/issues/2815).

### Évolutions techniques
- Suppression des recruiters (gestion des utilisateurs) [#2728](https://github.com/mission-apprentissage/labonnealternance/issues/2728).
- Mise à jour des habilitations pour une meilleure gestion des accès [#2878](https://github.com/mission-apprentissage/labonnealternance/issues/2878).
- Correction de bugs et améliorations de la stabilité de l'API et de l'interface utilisateur.
- Amélioration des performances de la recherche grâce à l'utilisation des lectures MongoDB sur les secondaires [#2849](https://github.com/mission-apprentissage/labonnealternance/issues/2849).
- Optimisation de la récurrence du rommage des offres [#2802](https://github.com/mission-apprentissage/labonnealternance/issues/2802).
- Correction de vulnérabilités critiques (handlebars, fast-xml-parser, basic-ftp) et mise à jour des dépendances [#2810](https://github.com/mission-apprentissage/labonnealternance/issues/2810).
- Amélioration de la gestion du rate limit de l'API job-étudiant [#2831](https://github.com/mission-apprentissage/labonnealternance/issues/2831).
- Stabilisation des healthchecks et réduction de la pression sur le stream processor [#2845](https://github.com/mission-apprentissage/labonnealternance/issues/2845).
- Correction de bugs Sentry dans l'interface utilisateur [#2807](https://github.com/mission-apprentissage/labonnealternance/issues/2807).
- Amélioration de la gestion des erreurs d'hydratation et du CLS sur la page d'accueil [#2814](https://github.com/mission-apprentissage/labonnealternance/issues/2814).
- Ajout d'un job de resynchronisation des stats LBA [#2846](https://github.com/mission-apprentissage/labonnealternance/issues/2846).

### Autres changements
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mise à jour de la documentation.
- Corrections SEO (canonical, meta descriptions, sitemap) [#2851](https://github.com/mission-apprentissage/labonnealternance/issues/2851).
- Correction de liens et de textes sur différentes pages [#2835](https://github.com/mission-apprentissage/labonnealternance/issues/2835).
- Correction de l'affichage des menus déroulants provenant de Notion [#2859](https://github.com/mission-apprentissage/labonnealternance/issues/2859).
- Correction de l'affichage du nombre de candidatures pour les offres partenaires [#2847](https://github.com/mission-apprentissage/labonnealternance/issues/2847).
- Correction de l'affichage des offres GEIQ et CFA [#2840](https://github.com/mission-apprentissage/labonnealternance/issues/2840).
- Correction de l'envoi des emails RDV [#2808](https://github.com/mission-apprentissage/labonnealternance/issues/2808).
- Correction du formatage de la description des offres Hellowork Buddi [#2763](https://github.com/mission-apprentissage/labonnealternance/issues/2763).
- Correction de la page FAQ [#2823](https://github.com/mission-apprentissage/labonnealternance/issues/2823).
- Correction de l'import des flux Kelio, Laposte et Leboncoin [#2827](https://github.com/mission-apprentissage/labonnealternance/issues/2827).
- Ajout d'un script d'analyse de la blocklist CFA [#2822](https://github.com/mission-apprentissage/labonnealternance/issues/2822).
