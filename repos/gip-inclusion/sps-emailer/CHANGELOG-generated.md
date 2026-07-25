## Changelog : sps-emailer (30 derniers jours, au 26 juin 2026)

### Résumé
Les récentes mises à jour de sps-emailer améliorent significativement le processus de gestion et d'envoi des recommandations SPS. Une nouvelle commande permet de purger les anciennes sorties nominatives, et la documentation a été enrichie pour faciliter l'utilisation et la configuration du projet.  L'implémentation d'un pipeline complet pour les emails SPS, incluant la conversion, l'anonymisation, le rendu et l'envoi via Brevo, est désormais disponible.

### Évolutions fonctionnelles
- Ajout d'une commande `sps purge` pour supprimer les anciennes sorties nominatives, avec une confirmation et une durée par défaut de 7 jours. [#1](https://github.com/gip-inclusion/sps-emailer/pull/1)
- Implémentation d'un pipeline complet pour les emails SPS : conversion, anonymisation, rendu et envoi via Brevo (avec tunnel SOCKS). [#1](https://github.com/gip-inclusion/sps-emailer/pull/1)

### Évolutions techniques
- Configuration de Dependabot pour la gestion des dépendances avec `uv`. [#2](https://github.com/gip-inclusion/sps-emailer/pull/2)
- Suppression des artefacts de session `superpowers/` et `upstream-agent-prompt` du dépôt.

### Autres changements
- Amélioration de la documentation README avec un guide pas-à-pas pour l'entrée JSON et la documentation des variables d'environnement requises.
- Simplification du README.
- Suppression de la conversion Markdown vers JSON du chemin nominal.
