## Changelog : quefairedemesobjets (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la recherche et de l'affichage des résultats, ainsi que sur la correction de bugs et l'optimisation des performances. Des efforts importants ont également été déployés pour la maintenance technique, incluant des mises à jour de dépendances et des améliorations de l'infrastructure. Un travail de fond sur la déduplication des données et le clustering a également été initié.

### Évolutions fonctionnelles
- Amélioration de la recherche : correction de l'affichage dupliqué du nom dans les résultats de recherche (notamment pour Vélovélo) [#2754].
- Tracking des clics sur les résultats de recherche implémenté [#2722].
- Correction de la page d'accueil de l'assistant, avec une refonte complète [#2572].
- Ajout de la sous-catégorie "Smartphone" au PAM pour les acteurs Ecologic et Ecosysteme [#2634].
- Correction d'un problème sur les couleurs dans la fiche acteur, qui reprenaient la couleur de l'action au lieu du groupe.
- Ajout de la distance dans le mode liste et la fiche acteur [#2632].
- Correction d'un bug sur le formulaire : la carte était masquée et le titre tronqué [#2632].
- Redirections massives depuis l'ancien site vers le nouveau implémentées [#2639].
- Affichage des liens des SIRET dans le clustering [#2649].

### Évolutions techniques
- Migration de base de données effectuée [#2750].
- Correction d'erreurs sur les termes de recherche orphelins [#2749].
- Optimisations de performances apportées [#2633].
- Passage de la version d'Airflow à la version 2 (rollback effectué suite à des problèmes) [#2646].
- Refactoring de la gestion du tableau des suggestions de groupe [#2619].
- Amélioration de l'indexation à la publication d'une page Wagtail [#2653].
- Suppression du script de migration de la page d'accueil [#2637].
- Rationalisation des environnements de développement [#2659].
- Documentation et Makefile pour la partie DBT ajoutés [#2631].
- Correction des tests e2e suite à des mises à jour de dépendances [#2736].
- Correction des tests après les mises à jour de Pandas [#2735].
- Mise à jour de nombreuses dépendances (Django, React, Parcel, PostgreSQL, Airflow, dbt, etc.).
- Amélioration de la résilience des tests e2e [#2661].

### Autres changements
- Redirection du domaine legacy vers le domaine principal [#2756].
- Proxy PostHog configuré via le domaine principal [#2720].
- Suppression de directives Nginx en double sur Scalingo [#2718].
- Ajout d'un avertissement si une page à rediriger existe déjà dans le CMS [#2701].
- Début de l'implémentation d'un modèle de Machine Learning pour la déduplication des données [#2727, #2662].
- Suppression de l'accent du code `mélange_d_inertes_produits` des sous-catégories [#2635].
- Suppression du cache npm car le `package-lock.json` est maintenant dans `webapp` [#2700].
- Suppression de l'icône bonus réparation incorrecte [#2660].
- Mise en place d'un système d'enrichissement des URL pour la nouvelle architecture de SuggestionGroupe [#2699].
- Correction de l'indexation des pages pour éviter la mise en cache incorrecte [#2629].
- Suppression de la mise en cache de la version iframe et standalone d'une page avec la même clé [#2629].
