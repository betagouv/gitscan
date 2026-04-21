## Changelog : quefairedemesobjets (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la stabilité et des performances de la plateforme, notamment en corrigeant des tests automatisés et en optimisant le code. Des améliorations ont également été apportées à l'expérience utilisateur, avec un suivi des clics sur les résultats de recherche et des corrections sur la page d'accueil de l'assistant. Des travaux préliminaires sur un modèle de machine learning pour la déduplication des données ont également été entrepris.

### Évolutions fonctionnelles
- **Suivi des clics sur les résultats de recherche:** Implémentation du suivi des clics sur les résultats de recherche pour mieux comprendre le comportement des utilisateurs. [#2722](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2722)
- **Refonte de la page d'accueil de l'assistant:** Amélioration de l'interface et de l'expérience utilisateur de la page d'accueil de l'assistant. [#2572](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2572)
- **Correction de bugs sur la fermeture d'une fiche acteur:** Résolution de problèmes empêchant la fermeture correcte des fiches acteurs. [#2622](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2622)
- **Ajout de la sous-catégorie "Smartphone" au PAM:** Ajout de la sous-catégorie "Smartphone" au Plan d'Action pour la Matière. [#2634](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2634)
- **Affichage des liens des SIRET, SIREN et URL:** Amélioration de l'affichage des informations de contact des acteurs. [#2655](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2655)
- **Correction sur les traductions et le plan de site:** Amélioration de la qualité des traductions et du plan de site. [#2625](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2625)

### Évolutions techniques
- **Corrections de tests:** Correction de plusieurs tests automatisés (e2e, unitaires) suite à des mises à jour de dépendances et des modifications du code. [#2735](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2735), [#2736](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2736)
- **Optimisations de performances:** Amélioration des performances globales de la plateforme. [#2633](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2633)
- **Modèle de Machine Learning pour la déduplication:** Premières itérations d'un modèle de machine learning pour la déduplication des données. [#2727](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2727), [#2662](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2662)
- **Mise à jour des dépendances:** Mise à jour de nombreuses dépendances (Django, React, Parcel, etc.) pour bénéficier des dernières corrections de bugs et améliorations de sécurité.
- **Refonte du tracking:** Refonte du système de tracking avec PostHog, incluant l'envoi d'événements et de vues de page. [#2721](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2721)
- **Proxy PostHog:** Configuration d'un proxy pour PostHog afin d'utiliser notre propre domaine. [#2720](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2720)

### Autres changements
- **Documentation DBT:** Ajout de documentation et d'un Makefile pour la partie DBT (Data Build Tool). [#2631](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2631)
- **Configuration Nginx:** Suppression de directives Nginx en double sur Scalingo. [#2718](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2718)
- **Exclusion de la page de configuration de l'infotri de l'index Google:** Ajout d'une balise meta robots pour exclure la page de configuration de l'index Google. [#2702](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2702)
- **Amélioration de l'indexation Wagtail:** Amélioration de l'indexation lors de la publication d'une page Wagtail. [#2653](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2653)
- **Rationalisation des environnements de développement:** Simplification et amélioration des environnements de développement. [#2659](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2659)
