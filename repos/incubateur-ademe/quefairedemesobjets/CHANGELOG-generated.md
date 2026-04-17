## Changelog : quefairedemesobjets (30 derniers jours, au 16 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la performance, la correction de bugs et l'amélioration de l'expérience utilisateur, notamment sur la page d'accueil de l'assistant et la fiche acteur. Des optimisations ont également été apportées à l'infrastructure et aux outils de développement.

### Évolutions fonctionnelles
- **Assistant :** Refonte complète de la page d'accueil pour une meilleure expérience utilisateur [#2572].
- **Fiche Acteur :**
    - Correction d'un bug empêchant la fermeture correcte des fiches acteur [#2622].
    - Affichage de la distance dans le mode liste et sur la fiche acteur [#2632].
    - Correction des couleurs sur la fiche acteur pour une meilleure lisibilité [#2654].
    - Ajout des liens des SIRET, SIREN et URL sur la fiche acteur [#2655].
    - Correction du mapping des identifiants de formulaire sur la fiche acteur [#2695].
- **Cartographie :** Amélioration du clustering pour gérer les latitudes et longitudes identiques [#2703].
- **Redirections :** Mise en place de redirections massives depuis l'ancien site vers le nouveau [#2639].
- **CMS :** Ajout d'un avertissement si une page à rediriger existe déjà dans le CMS [#2701].
- **Indexation :** Amélioration de l'indexation des pages Wagtail lors de leur publication [#2653].
- **Catégories :** Ajout de la sous-catégorie "Smartphone" au PAM pour les filières Ecologic et Ecosysteme [#2634].

### Évolutions techniques
- **Performance :** Optimisations générales des performances [#2633, 9b378b3].
- **Infrastructure :**
    - Proxy PostHog via le domaine du projet pour une meilleure confidentialité [#2720].
    - Suppression de directives Nginx en double sur Scalingo [#2718].
    - Rationalisation des environnements de développement [#2659].
- **Tests :**
    - Correction d'un problème de tests e2e après le renommage des tables de cache [#2717].
    - Correction de la recherche dans les tests e2e [#2680].
    - Amélioration de la résilience d'un test e2e [#2661].
- **Airflow :** Retour à une version antérieure d'Airflow [#2646].
- **DBT :** Documentation et Makefile pour la partie DBT [#2631].
- **Cache :** Correction d'un problème lié au cache npm [#2700].
- **Django Modelsearch :** Utilisation de la dernière version de django-modelsearch avec gestion des accents [#2643].

### Autres changements
- Exclusion de la page de configuration de l'infotri de l'indexation Google [#2702].
- Correction d'un bug sur les traductions et le plan du site [#2625].
- Suppression du script de backup de la base de données en local [#2627].
- Suppression du warning lié à la colonne delete de l'export des sous-catégories [#2618].
- Correction d'un problème de lecture de la première ligne du CSV [#2630].
- Suppression de l'accent dans le code `melange_d_inertes_produits…` des sous-catégories [#2635].
- Correction du lien du logo [#2626].
- Diverses mises à jour de dépendances (voir commits individuels).
