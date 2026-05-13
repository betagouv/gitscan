## Changelog : quefairedemesobjets (30 derniers jours, au 12 mai 2026)

### Résumé
Le projet a connu une période d'activité soutenue ces dernières semaines, avec des améliorations significatives de l'expérience utilisateur, notamment sur la carte et les résultats de recherche. Des efforts importants ont également été consacrés à l'optimisation des performances, à la correction de bugs et à la mise à jour des dépendances pour assurer la stabilité et la sécurité de la plateforme. Des travaux préliminaires sur la déduplication d'objets via du machine learning ont également été entrepris.

### Évolutions fonctionnelles
- **Carte :**
    - La mini-carte est désormais affichée sur mobile dans la fiche détaillée d'un objet [#2797](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2797).
    - Correction de l'affichage dupliqué du nom dans les résultats de recherche Vélovélo [#2754](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2754).
- **Recherche :**
    - Ajout du tracking des clics sur les résultats de recherche [#2722](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2722).
    - Possibilité de clusteriser les résultats par distance exprimée en mètres [#2728](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2728).
- **Nouvelle fonctionnalité :**
    - Ajout d'une Source générique configurable pour répondre à des besoins spécifiques [#2466](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2466).
- **Redirection :**
    - Redirection du domaine legacy vers le domaine principal [#2756](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2756).

### Évolutions techniques
- **Performances :** Optimisations de performances générales de la plateforme [#2633](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2633).
- **Déploiement :** Suppression de la nécessité de déployer un container après une mise à jour [#2724](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2724).
- **Clustering :**  Première itération d'un modèle de Machine Learning pour la déduplication d'objets [#2662](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2662).
- **Infrastructure :** Correction d'un problème de cache npm [#2700](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2700).
- **Mises à jour de dépendances :** De nombreuses dépendances ont été mises à jour (Django, React, Airflow, dbt, etc.) pour améliorer la sécurité et la stabilité. (Voir les commits individuels pour plus de détails).

### Autres changements
- **Documentation :** Amélioration de la documentation et de la configuration.
- **Tests :** Correction de tests e2e suite à des mises à jour de dépendances [#2736](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2736) et [#2760](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2760).
- **Analytics :** Refonte du tracking avec l'implémentation de pageView et d'événements [#2721](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2721).
- **SEO :** Exclusion de la page de configuration de l'infotri de l'index Google [#2702](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2702).
- **Configuration :** Suppression de directives Nginx en double sur Scalingo [#2718](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2718).
- **Correction de bugs :** Correction d'une erreur sur les termes de recherche orphelins [#2749](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2749).
- **Health Check :** Amélioration de la gestion des health checks [#2763](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2763).
- **Suggestion Groupe :** Correction d'un bug empêchant la bonne édition des valeurs [#2802](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2802).
