## Changelog : n8n-nodes-playwright-core (30 derniers jours, au 27 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des instances Playwright distantes, notamment avec l'introduction d'un nouveau nœud "Claim" permettant de réserver et de libérer des instances.  De plus, la prise en charge des proxys a été ajoutée pour une plus grande flexibilité dans les configurations réseau.

### Évolutions fonctionnelles
- **Nouveau nœud "Claim"**: Ajout d'un nœud permettant de gérer le cycle de vie des instances Playwright distantes (réservation, renouvellement, libération) [#15](https://github.com/IA-Generative/n8n-nodes-playwright-core/pull/15) et [#16](https://github.com/IA-Generative/n8n-nodes-playwright-core/pull/16).
- **Support des proxys**:  Possibilité de configurer et d'utiliser des proxys pour les contextes Playwright, permettant de router le trafic via différents serveurs. [#15](https://github.com/IA-Generative/n8n-nodes-playwright-core/pull/15)
- **Sélection de proxy par protocole**:  Possibilité de sélectionner un proxy en fonction du protocole (http/https) de l'URL cible.
- **Ajout d'un header de session**: Ajout d'un header de session à l'opération de "Claim" pour une meilleure identification des instances.

### Évolutions techniques
- **Refactoring du contrôleur "Claim"**:  Amélioration de la structure du contrôleur "Claim" pour une meilleure organisation et maintenabilité.
- **Propagation du proxy**: Le proxy configuré est maintenant correctement propagé au navigateur Playwright.

### Autres changements
- Correction d'un bug où le nœud "Claim" n'était pas affiché dans n8n. [#16](https://github.com/IA-Generative/n8n-nodes-playwright-core/issues/16)
- Mise à jour de la version du package.
