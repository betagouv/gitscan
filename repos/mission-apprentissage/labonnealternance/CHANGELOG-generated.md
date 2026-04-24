## Changelog : labonnealternance (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la recherche d'offres, la candidature et la gestion des offres partenaires. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Amélioration de la navigation sur la page des résultats de recherche, permettant une meilleure expérience utilisateur. [#2861](https://github.com/mission-apprentissage/labonnealternance/issues/2861)
- Possibilité de candidatures spontanées sans adresse email, en utilisant uniquement un numéro de téléphone. [#2863](https://github.com/mission-apprentissage/labonnealternance/issues/2863)
- Intégration d'une clé API Taleez pour faciliter les candidatures. [#2873](https://github.com/mission-apprentissage/labonnealternance/issues/2873)
- Amélioration de l'affichage du nombre de candidatures pour les offres partenaires. [#2867](https://github.com/mission-apprentissage/labonnealternance/issues/2867)
- Correction de l'affichage de la modale d'application pour les offres partenaires externes. [#2870](https://github.com/mission-apprentissage/labonnealternance/issues/2870)
- Amélioration du CTA "Je postule" sur les offres. [#2850](https://github.com/mission-apprentissage/labonnealternance/issues/2850)
- Ajout d'une whitelist pour les offres des GEIQ et des CFA d'entreprise. [#2840](https://github.com/mission-apprentissage/labonnealternance/issues/2840)
- Intégration d'une landing page pour la campagne "1 jour 1 solution". [#2834](https://github.com/mission-apprentissage/labonnealternance/issues/2834)
- Ajout de liens vers LinkedIn pour la DGEFP. [#2842](https://github.com/mission-apprentissage/labonnealternance/issues/2842)
- Ajout de blocs salaires sur les pages SEO métiers et redirection vers le simulateur de rémunération. [#2785](https://github.com/mission-apprentissage/labonnealternance/issues/2785)
- Suppression de la carte sur la page de recherche. [#2790](https://github.com/mission-apprentissage/labonnealternance/issues/2790)
- Ajout de rubriques vers Mon Logement Étudiant. [#2793](https://github.com/mission-apprentissage/labonnealternance/issues/2793)
- Modification de l'article concernant le handicap. [#2816](https://github.com/mission-apprentissage/labonnealternance/issues/2816)
- Ajout de flux d'import pour EDF et Enedis. [#2819](https://github.com/mission-apprentissage/labonnealternance/issues/2819)
- Amélioration de l'affichage correct de la modale de candidature sur Taleez. [#2865](https://github.com/mission-apprentissage/labonnealternance/issues/2865)
- Ajout du tracking Matomo sur la simulation. [#2832](https://github.com/mission-apprentissage/labonnealternance/issues/2832)
- Amélioration du texte et des images pour la RCO (Reconnaissance des acquis de l'expérience). [#2860](https://github.com/mission-apprentissage/labonnealternance/issues/2860)

### Évolutions techniques
- Suppression des recruiters. [#2728](https://github.com/mission-apprentissage/labonnealternance/issues/2728)
- Ajout d'un job de resynchronisation des statistiques LBA. [#2846](https://github.com/mission-apprentissage/labonnealternance/issues/2846)
- Correction de la recherche de formations. [#2868](https://github.com/mission-apprentissage/labonnealternance/issues/2868)
- Amélioration de la gestion des requêtes N+1 sur l'API training links. [#2841](https://github.com/mission-apprentissage/labonnealternance/issues/2841)
- Optimisation des healthchecks et réduction de la pression sur le stream processor. [#2845](https://github.com/mission-apprentissage/labonnealternance/issues/2845)
- Amélioration de la gestion du rate limit de l'API job-étudiant avec retry et throttling proactif. [#2831](https://github.com/mission-apprentissage/labonnealternance/issues/2831)
- Ajout de lectures MongoDB sur les secondaires pour la recherche. [#2849](https://github.com/mission-apprentissage/labonnealternance/issues/2849)
- Correction de bugs et mises à jour de sécurité (handlebars, fast-xml-parser, basic-ftp). [#2810](https://github.com/mission-apprentissage/labonnealternance/issues/2810)
- Amélioration de la gestion des erreurs et des logs.
- Correction de problèmes de CLS et d'hydratation sur la page d'accueil. [#2814](https://github.com/mission-apprentissage/labonnealternance/issues/2814)
- Ajout de tests et amélioration de la couverture de code.

### Autres changements
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Mise à jour de la documentation.
- Correction des notes des partenaires. [#2839](https://github.com/mission-apprentissage/labonnealternance/issues/2839)
- Correction de liens et de textes.
- Amélioration du SEO (meta descriptions, canonical, sitemap). [#2851](https://github.com/mission-apprentissage/labonnealternance/issues/2851)
- Correction de l'affichage des menus déroulants provenant de Notion. [#2859](https://github.com/mission-apprentissage/labonnealternance/issues/2859)
- Correction de l'affichage des offres de formation.
- Suppression de la whitelist IP temporaire du stress test. [#2854](https://github.com/mission-apprentissage/labonnealternance/issues/2854)
- Correction de la gestion des contrats manquants sur les flux Kelio, Laposte et Leboncoin. [#2827](https://github.com/mission-apprentissage/labonnealternance/issues/2827)
- Ajout d'un script d'analyse de la blocklist CFA dans computed_jobs_partners. [#2822](https://github.com/mission-apprentissage/labonnealternance/issues/2822)
- Correction de l'envoi des emails RDV bloqués. [#2808](https://github.com/mission-apprentissage/labonnealternance/issues/2808)
- Correction de l'export Cegid. [#2771](https://github.com/mission-apprentissage/labonnealternance/issues/2771)
- Correction d'une erreur objectId. [#2776](https://github.com/mission-apprentissage/labonnealternance/issues/2776)
