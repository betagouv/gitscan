## Changelog : cdata (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'améliorations notables pour faciliter la recherche et la consultation des données, notamment via une meilleure gestion des attributions et des filtres. Des optimisations techniques importantes ont également été réalisées pour accélérer le chargement des pages et stabiliser l'interface utilisateur.

### Évolutions fonctionnelles
- Extension de l'attribution des points de contact aux jeux de données et services de données [#1189].
- Amélioration de l'interface de sélection de la fréquence de mise à jour, avec un regroupement des fréquences principales [#1202].
- Tri des avis de la CADA par date d'audience (du plus récent au plus ancien) [#1183].
- Ajout du logo Numérique.gouv dans le pied de page [#1203].
- Corrections d'interface et de contenu : uniformisation des labels de filtres [#1107], correction de typos en français [#1205], et maintien de l'onglet actif lors de l'ajout de paramètres d'URL [#1185].
- Amélioration de la robustesse de la navigation : gestion propre des erreurs 404 pour les pages inexistantes [#1199] et des ressources supprimées [#1201].
- Sécurisation des liens de téléchargement en ne proposant que les protocoles http(s) [#1195].

### Évolutions techniques
- **Optimisation des performances** : Mise en place de stratégies de mise en cache pour les pages et les données du site, et réduction des appels API inutiles pour les utilisateurs anonymes [#1200, #1191, #1190, #1192].
- **Stabilité de l'interface** : Résolution de plusieurs problèmes d'affichage (mismatch d'hydratation) liés aux dates, au menu de recherche mobile et aux éléments de survol [#1198, #1197, #1208].
- **CI/CD & Infrastructure** : Optimisation des processus de publication des composants, configuration générique du registre de conteneurs et mise à jour du sitemap via udata [#1206, #1187, #1176].
- **Routage & SEO** : Amélioration de l'indexation en excluant les listes filtrées et correction du routage des liens API [#1186, #1196].

### Autres changements
- Correction de traductions manquantes [#1181].
