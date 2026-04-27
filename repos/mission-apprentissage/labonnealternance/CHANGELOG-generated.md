## Changelog : labonnealternance (30 derniers jours, au 2026-04-24)

### Résumé
Les dernières mises à jour de la plateforme La Bonne Alternance se concentrent sur l'amélioration de l'expérience utilisateur, notamment en matière de recherche et de candidature, ainsi que sur l'ajout de nouvelles fonctionnalités comme l'intégration de Taleez et de nouveaux flux d'offres. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout de 10 nouvelles pages ville optimisées pour le SEO. [#2875](https://github.com/mission-apprentissage/labonnealternance/issues/2875)
- Amélioration de la navigation sur la page de résultats de recherche. [#2861](https://github.com/mission-apprentissage/labonnealternance/issues/2861)
- Possibilité de candidater spontanément sans adresse email, en fournissant un numéro de téléphone. [#2863](https://github.com/mission-apprentissage/labonnealternance/issues/2863)
- Intégration de l'API Taleez pour les candidatures. [#2873](https://github.com/mission-apprentissage/labonnealternance/issues/2873)
- Amélioration de l'affichage du nombre de candidatures pour les offres partenaires. [#2867](https://github.com/mission-apprentissage/labonnealternance/issues/2867)
- Correction du décalage lors du scroll vers la première candidature spontanée. [#2874](https://github.com/mission-apprentissage/labonnealternance/issues/2874)
- Amélioration de l'affichage de la modale d'application pour les offres partenaires externes. [#2870](https://github.com/mission-apprentissage/labonnealternance/issues/2870)
- Correction du CTA "Je postule" sur les offres. [#2850](https://github.com/mission-apprentissage/labonnealternance/issues/2850)
- Ajout d'une whitelist pour les offres des GEIQ et des CFA d'entreprise. [#2840](https://github.com/mission-apprentissage/labonnealternance/issues/2840)
- Ajout d'une landing page pour la campagne "1 jour 1 solution". [#2834](https://github.com/mission-apprentissage/labonnealternance/issues/2834)
- Ajout de liens vers LinkedIn pour la DGEFP. [#2842](https://github.com/mission-apprentissage/labonnealternance/issues/2842)
- Ajout de flux d'import pour EDF et Enedis. [#2819](https://github.com/mission-apprentissage/labonnealternance/issues/2819)
- Ajout de blocs salaires sur les pages SEO des métiers et redirection vers le simulateur de rémunération. [#2785](https://github.com/mission-apprentissage/labonnealternance/issues/2785)
- Ajout de rubriques vers Mon Logement Étudiant. [#2793](https://github.com/mission-apprentissage/labonnealternance/issues/2793)
- Modification de l'article sur le handicap. [#2816](https://github.com/mission-apprentissage/labonnealternance/issues/2816)
- Ajout d'un formulaire Tally sur la page de recherche. [#2817](https://github.com/mission-apprentissage/labonnealternance/issues/2817)
- Mise à jour du plan du site. [#2838](https://github.com/mission-apprentissage/labonnealternance/issues/2838)
- Ajout de filtres par type de candidature (tags). [#2815](https://github.com/mission-apprentissage/labonnealternance/issues/2815)

### Évolutions techniques
- Suppression des recruiters. [#2728](https://github.com/mission-apprentissage/labonnealternance/issues/2728)
- Ajout d'un job de resynchronisation des statistiques LBA. [#2846](https://github.com/mission-apprentissage/labonnealternance/issues/2846)
- Amélioration de la gestion des offres privées (correction du type de contrat manquant). [#2827](https://github.com/mission-apprentissage/labonnealternance/issues/2827)
- Optimisation des requêtes pour éviter les problèmes de performance (N+1) sur l'API training links. [#2841](https://github.com/mission-apprentissage/labonnealternance/issues/2841)
- Amélioration de la récurrence du rommage des offres. [#2802](https://github.com/mission-apprentissage/labonnealternance/issues/2802)
- Ajout de lectures sur les secondaires MongoDB pour la recherche. [#2849](https://github.com/mission-apprentissage/labonnealternance/issues/2849)
- Stabilisation des healthchecks et réduction de la pression sur le stream processor. [#2845](https://github.com/mission-apprentissage/labonnealternance/issues/2845)
- Correction de bugs et mises à jour de sécurité (handlebars, fast-xml-parser, basic-ftp). [#2810](https://github.com/mission-apprentissage/labonnealternance/issues/2810)
- Amélioration de la gestion du rate limit de l'API job-étudiant avec retry et throttling proactif. [#2831](https://github.com/mission-apprentissage/labonnealternance/issues/2831)
- Correction de bugs et amélioration de la performance sur la page d'accueil (CLS et hydration). [#2814](https://github.com/mission-apprentissage/labonnealternance/issues/2814)

### Autres changements
- Corrections de bugs mineurs et améliorations de l'accessibilité.
- Mise à jour des notes des partenaires. [#2839](https://github.com/mission-apprentissage/labonnealternance/issues/2839)
- Correction de liens et de textes (RCO, FAQ, Grand Est).
- Amélioration du SEO (canonical, meta descriptions, sitemap).
- Correction de problèmes d'affichage des menus déroulants provenant de Notion. [#2859](https://github.com/mission-apprentissage/labonnealternance/issues/2859)
- Correction de l'affichage du nombre de candidatures pour les jobs partenaires. [#2870](https://github.com/mission-apprentissage/labonnealternance/issues/2870)
- Correction de l'envoi des emails RDV. [#580](https://github.com/mission-apprentissage/labonnealternance/issues/580)
- Ajout d'un script d'analyse de la blocklist CFA. [#2822](https://github.com/mission-apprentissage/labonnealternance/issues/2822)
