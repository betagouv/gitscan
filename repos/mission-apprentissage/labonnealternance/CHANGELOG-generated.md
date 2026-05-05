## Changelog : labonnealternance (30 derniers jours, au 2026-05-04)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment au niveau de la recherche d'offres et de la gestion des candidatures. Des optimisations ont également été apportées pour améliorer la performance et la stabilité de la plateforme, ainsi que pour renforcer le SEO et le suivi des données via Matomo.

### Évolutions fonctionnelles
- **Recherche et Affichage des offres :**
    - Réordonnancement des offres en fonction du statut mandataire. [#2888](https://github.com/mission-apprentissage/labonnealternance/issues/2888)
    - Suppression du composant "EnqueteTally" de la page de recherche pour simplifier l'interface. [#2886](https://github.com/mission-apprentissage/labonnealternance/issues/2886)
    - Ajout d'un champ de description et amélioration de l'affichage des détails des offres pour les recruteurs. [#2881](https://github.com/mission-apprentissage/labonnealternance/issues/2881)
    - Amélioration de la gestion de la géolocalisation pour éviter les erreurs liées au cache. [#2884](https://github.com/mission-apprentissage/labonnealternance/issues/2884)
- **Candidatures :**
    - Amélioration de la navigation sur la page de résultats de recherche. [#2861](https://github.com/mission-apprentissage/labonnealternance/issues/2861)
    - Possibilité de candider spontanément avec un numéro de téléphone si l'adresse e-mail n'est pas disponible. [#2863](https://github.com/mission-apprentissage/labonnealternance/issues/2863)
    - Amélioration de l'affichage du nombre de candidatures pour les offres partenaires. [#2867](https://github.com/mission-apprentissage/labonnealternance/issues/2867)
    - Correction de l'affichage de la modale de candidature sur Taleez. [#2865](https://github.com/mission-apprentissage/labonnealternance/issues/2865)
    - Amélioration du CTA "Je postule" sur les offres. [#2850](https://github.com/mission-apprentissage/labonnealternance/issues/2850)
    - Précision du scroll vers la première candidature spontanée. [#2874](https://github.com/mission-apprentissage/labonnealternance/issues/2874)
- **SEO et Contenu :**
    - Ajout de 10 nouvelles pages ville pour améliorer le référencement. [#2872](https://github.com/mission-apprentissage/labonnealternance/issues/2872) et [#2875](https://github.com/mission-apprentissage/labonnealternance/issues/2875)
    - Exclure les offres des entreprises partenaires reçues en direct du SEO. [#2813](https://github.com/mission-apprentissage/labonnealternance/issues/2813)
    - Mise à jour du texte et des images de la page RCO. [#2860](https://github.com/mission-apprentissage/labonnealternance/issues/2860)
    - Ajout de blocs salaires sur les pages SEO des métiers et redirection vers le simulateur de rémunération. [#2785](https://github.com/mission-apprentissage/labonnealternance/issues/2785)
- **Partenaires :**
    - Ajout de la clé API Taleez. [#2873](https://github.com/mission-apprentissage/labonnealternance/issues/2873)
    - Ajout de flux import pour EDF et Enedis. [#2728](https://github.com/mission-apprentissage/labonnealternance/issues/2728) et [#2819](https://github.com/mission-apprentissage/labonnealternance/issues/2819)
    - Whitelist des offres des GEIQ et des CFA d'entreprise. [#2840](https://github.com/mission-apprentissage/labonnealternance/issues/2840)

### Évolutions techniques
- **Tracking et Analytics :**
    - Ajout du tracking Matomo pour la recherche, la découverte et les candidatures. [#2871](https://github.com/mission-apprentissage/labonnealternance/issues/2871)
    - Ajout du tracking Matomo sur la simulation. [#2832](https://github.com/mission-apprentissage/labonnealternance/issues/2832)
    - Tracking des candidatures partenaires externes. [#2862](https://github.com/mission-apprentissage/labonnealternance/issues/2862)
- **Performance et Infrastructure :**
    - Ajout de lectures MongoDB sur les secondaires pour la recherche. [#2849](https://github.com/mission-apprentissage/labonnealternance/issues/2849)
    - Stabilisation des healthchecks et réduction de la pression du stream processor. [#2845](https://github.com/mission-apprentissage/labonnealternance/issues/2845)
    - Optimisation de la gestion du rate limit de l'API job-étudiant avec retry et throttling proactif. [#2831](https://github.com/mission-apprentissage/labonnealternance/issues/2831)
    - Amélioration de la configuration de MongoDB (maxPoolSize, secondary helper). [#2856](https://github.com/mission-apprentissage/labonnealternance/issues/2856)
    - Ajout d'un job de resynchronisation des stats LBA. [#2846](https://github.com/mission-apprentissage/labonnealternance/issues/2846)
- **Refactoring et Maintenance :**
    - Suppression du code lié aux recruiters. [#2728](https://github.com/mission-apprentissage/labonnealternance/issues/2728)
    - Suppression des requêtes N+1 sur l'API training links. [#2841](https://github.com/mission-apprentissage/labonnealternance/issues/2841)

### Autres changements
- Mise à jour des habilitations. [#2878](https://github.com/mission-apprentissage/labonnealternance/issues/2878)
- Correction de valeurs vides pour le SEO Google Search. [#2883](https://github.com/mission-apprentissage/labonnealternance/issues/2883)
- Mise à jour de la liste des CFA et ajout d'un test pour expliquer les blocages. [#2879](https://github.com/mission-apprentissage/labonnealternance/issues/2879)
- Correction de l'origine des jobs partenaires. [#2880](https://github.com/mission-apprentissage/labonnealternance/issues/2880)
- Correction de la modification des champs utilisateur dans l'admin et l'opco. [#2869](https://github.com/mission-apprentissage/labonnealternance/issues/2869)
- Correction de l'envoi de mail de mer aux CFA. [#2808](https://github.com/mission-apprentissage/labonnealternance/issues/2808)
- Correction des liens vers les CFA. [#2843](https://github.com/mission-apprentissage/labonnealternance/issues/2843)
- Correction du bug des menus déroulants provenant de Notion. [#2859](https://github.com/mission-apprentissage/labonnealternance/issues/2859)
- Correction de l'affichage du nombre de candidatures pour les jobs partenaires. [#2867](https://github.com/mission-apprentissage/labonnealternance/issues/2867)
- Correction de la recherche de formations. [#2868](https://github.com/mission-apprentissage/labonnealternance/issues/2868)
- Correction de l'UI de la modale partner job external apply. [#2870](https://github.com/mission-apprentissage/labonnealternance/issues/2870)
- Correction de l'affichage du nombre de candidatures pour les offres avec smart apply. [#2848](https://github.com/mission-apprentissage/labonnealternance/issues/2848)
- Correction du formatage de la description des offres Hellowork Buddi. [#2858](https://github.com/mission-apprentissage/labonnealternance/issues/2858)
- Mise à jour des notes des partenaires. [#2839](https://github.com/mission-apprentissage/labonnealternance/issues/2839)
- Correction de la blacklist des CFA. [#2833](https://github.com/mission-apprentissage/labonnealternance/issues/2833)
- Correction du lien vers le Grand Est. [#2835](https://github.com/mission-apprentissage/labonnealternance/issues/2835)
