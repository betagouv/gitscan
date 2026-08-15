## Changelog : grist-core (30 derniers jours, au 21 juillet 2026)

### Résumé
Les récentes mises à jour de Grist se concentrent sur la personnalisation de l'interface utilisateur, notamment via de nouvelles options d'affichage des lignes, et sur le renforcement de la stabilité de l'infrastructure. Des améliorations ont également été apportées pour fluidifier la saisie de données et affiner le rendu visuel des cellules.

### Évolutions fonctionnelles
- Nouvelle option permettant de masquer les numéros de ligne ou d'afficher les identifiants de ligne (rowIDs) dans la grille [#2448](https://github.com/gristgouv/grist-core/issues/2448).
- Amélioration de l'expérience de saisie dans l'éditeur de choix pour garantir sa disponibilité avant la frappe au clavier [#2474](https://github.com/gristgouv/grist-core/issues/2474).
- Correction de l'affichage des cellules Markdown pour un rendu plus cohérent [#2465](https://github.com/gristgouv/grist-core/issues/2465).

### Évolutions techniques
- Introduction du proxying Grist Fleet entre les serveurs pour optimiser la gestion du trafic.
- Correction d'un plantage (crash) de la fonction `proxyHttpRequest` lors de la déconnexion d'un client.
- Nettoyage du code via la suppression d'un avertissement de lint sur l'union `ServerMode` [#2473](https://github.com/gristgouv/grist-core/issues/2473).

### Autres changements
- Amélioration de la documentation technique concernant la base de données [#2458](https://github.com/gristgouv/grist-core/issues/2458).
- Expansion du support linguistique avec l'ajout de traductions (Japonais, Suédois) et la mise à jour des clés de traduction [#2471](https://github.com/gristgouv/grist-core/issues/2471).
