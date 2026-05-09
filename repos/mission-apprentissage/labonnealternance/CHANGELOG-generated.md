## Changelog : labonnealternance (30 derniers jours, au 7 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de la recherche d'alternances, notamment l'ajout de critères de tri, l'intégration de nouveaux flux d'offres (EDF, Enedis, Taleez), et l'optimisation des performances. Des corrections ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier sur la page de recherche et l'application mobile. L'équipe a également travaillé sur l'ajout de pages SEO pour améliorer la visibilité du site.

### Évolutions fonctionnelles
- **Recherche :**
    - Ajout du tri des offres d'alternance selon le statut mandataire [#2888](https://github.com/mission-apprentissage/labonnealternance/issues/2888).
    - Exclusion des offres des entreprises partenaires reçues directement [#2813](https://github.com/mission-apprentissage/labonnealternance/issues/2813).
    - Amélioration de la recherche de formations [#2880](https://github.com/mission-apprentissage/labonnealternance/issues/2880).
    - Ajout de la navigation sur la page de résultats de recherche [#2861](https://github.com/mission-apprentissage/labonnealternance/issues/2861).
    - Amélioration du scroll vers la première candidature spontanée [#2874](https://github.com/mission-apprentissage/labonnealternance/issues/2874).
- **Offres d'emploi :**
    - Ajout du champ description et refonte de l'affichage du détail des offres pour les recruteurs [#2881](https://github.com/mission-apprentissage/labonnealternance/issues/2881).
    - Affichage correct du nombre de candidatures pour les offres partenaires [#2867](https://github.com/mission-apprentissage/labonnealternance/issues/2867).
    - Amélioration de la modale de candidature sur Taleez [#2865](https://github.com/mission-apprentissage/labonnealternance/issues/2865).
    - Ajout de la candidature directe vers Taleez [#2804](https://github.com/mission-apprentissage/labonnealternance/issues/2804).
    - Tracking des candidatures partenaires externes [#2862](https://github.com/mission-apprentissage/labonnealternance/issues/2862).
- **Intégrations :**
    - Intégration des flux d'offres EDF et Enedis [#2819](https://github.com/mission-apprentissage/labonnealternance/issues/2819).
    - Intégration de l'API Taleez avec une clé API dédiée [#2873](https://github.com/mission-apprentissage/labonnealternance/issues/2873).
- **SEO :**
    - Ajout de 10 nouvelles pages ville pour le SEO [#2872](https://github.com/mission-apprentissage/labonnealternance/issues/2872) et [#2875](https://github.com/mission-apprentissage/labonnealternance/issues/2875).
    - Amélioration du SEO pour les offres Google Search (correction des valeurs vides) [#2883](https://github.com/mission-apprentissage/labonnealternance/issues/2883).
- **Divers :**
    - Mise à jour des notes des partenaires [#2839](https://github.com/mission-apprentissage/labonnealternance/issues/2839).
    - Ajout d'un bloc salaires sur les pages SEO métiers et redirection vers le simulateur de rémunération [#2785](https://github.com/mission-apprentissage/labonnealternance/issues/2785).
    - Ajout de rubriques vers Mon Logement Étudiant [#2793](https://github.com/mission-apprentissage/labonnealternance/issues/2793).

### Évolutions techniques
- **Performance :**
    - Optimisation de la gestion des requêtes pour éviter les N+1 sur l'API training links [#2841](https://github.com/mission-apprentissage/labonnealternance/issues/2841).
    - Stabilisation des healthchecks et réduction de la pression du stream processor [#2845](https://github.com/mission-apprentissage/labonnealternance/issues/2845).
    - Ajout de lectures MongoDB sur les secondaires pour la recherche [#2849](https://github.com/mission-apprentissage/labonnealternance/issues/2849).
    - Gestion du rate limit 429 sur l'API job-étudiant avec retry et throttling proactif [#2831](https://github.com/mission-apprentissage/labonnealternance/issues/2831).
- **Infrastructure :**
    - Mise à jour des habilitations [#2878](https://github.com/mission-apprentissage/labonnealternance/issues/2878).
    - Configuration de MongoDB (maxPoolSize, secondary helper) [#2856](https://github.com/mission-apprentissage/labonnealternance/issues/2856).
- **Tracking :**
    - Ajout du tracking Matomo pour la recherche, la découverte et les candidatures [#2871](https://github.com/mission-apprentissage/labonnealternance/issues/2871).
    - Ajout du tracking Matomo sur la simulation [#2832](https://github.com/mission-apprentissage/labonnealternance/issues/2832).
- **Automatisation :**
    - Ajout d'un job de resynchronisation des stats LBA [#2846](https://github.com/mission-apprentissage/labonnealternance/issues/2846).

### Autres changements
- Correction de bugs mineurs liés à l'affichage des menus déroulants provenant de Notion [#2859](https://github.com/mission-apprentissage/labonnealternance/issues/2859).
- Suppression du composant EnqueteTally de la page recherche [#2886](https://github.com/mission-apprentissage/labonnealternance/issues/2886).
- Correction de l'affichage du nombre de candidatures pour les jobs partenaires [#2867](https://github.com/mission-apprentissage/labonnealternance/issues/2867).
- Correction de l'origine des jobs partenaires [#2880](https://github.com/mission-apprentissage/labonnealternance/issues/2880).
- Correction de la vérification du cache de géolocalisation [#2884](https://github.com/mission-apprentissage/labonnealternance/issues/2884).
- Mise à jour de la liste des CFA et ajout d'un test d'explication de blocage des CFA [#2879](https://github.com/mission-apprentissage/labonnealternance/issues/2879).
- Suppression des recruiters [#2728](https://github.com/mission-apprentissage/labonnealternance/issues/2728).
- Suppression de la carte dans la recherche LBA [#2790](https://github.com/mission-apprentissage/labonnealternance/issues/2790).
- Correction de la modification des champs utilisateur dans l'admin et l'opco [#2869](https://github.com/mission-apprentissage/labonnealternance/issues/2869).
- Correction de l'envoi des emails RDV bloqués [#580](https://github.com/mission-apprentissage/labonnealternance/issues/580).
- Correction du formatage de la description des offres Hellowork Buddi [#2843](https://github.com/mission-apprentissage/labonnealternance/issues/2843).
- Correction de l'envoi des emails RDV aux CFA [#2808](https://github.com/mission-apprentissage/labonnealternance/issues/2808).
- Correction des liens Google sur ville et code postal seulement [#2835](https://github.com/mission-apprentissage/labonnealternance/issues/2835).
- Correction de la priorité de `human_verification` dans `getClassificationFromLab` [#2836](https://github.com/mission-apprentissage/labonnealternance/issues/2836).
- Correction des robots.txt et canonical guides [#2851](https://github.com/mission-apprentissage/labonnealternance/issues/2851).
