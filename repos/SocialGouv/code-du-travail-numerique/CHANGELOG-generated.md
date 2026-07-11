## Changelog : code-du-travail-numerique (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette version apporte des corrections de bugs, notamment concernant l'affichage des accords et des tableaux, ainsi que des améliorations de la recherche et de la gestion des erreurs. De nouvelles fonctionnalités ont été ajoutées, comme un widget de notation pour les contributions et un système d'extraction d'événements pour le suivi analytique.

### Évolutions fonctionnelles
- Ajout d'un widget de notation pour les contributions ([#7344](https://github.com/SocialGouv/code-du-travail-numerique/issues/7344)).
- Correction de l'utilisation de l'API Legifrance pour les accords ([#7381](https://github.com/SocialGouv/code-du-travail-numerique/issues/7381)).
- Correction de l'affichage des entêtes de tableaux dans les contributions ([#7325](https://github.com/SocialGouv/code-du-travail-numerique/issues/7325)).
- Correction du bouton de fermeture du mode plein écran sur les tableaux ([#7373](https://github.com/SocialGouv/code-du-travail-numerique/issues/7373)).
- Ajout du type "bon à savoir" pour les contributions ([#7326](https://github.com/SocialGouv/code-du-travail-numerique/issues/7326)).
- Correction de la redirection de l'ancienne fiche canicule vers la nouvelle page d'information ([#7322](https://github.com/SocialGouv/code-du-travail-numerique/issues/7322), [#7318](https://github.com/SocialGouv/code-du-travail-numerique/issues/7318)).
- Normalisation de l'affichage du code IDCC 9999 dans les conventions collectives ([#7303](https://github.com/SocialGouv/code-du-travail-numerique/issues/7303)).
- Suppression de la balise canonical sur la page générique des contributions ([#7316](https://github.com/SocialGouv/code-du-travail-numerique/issues/7316)).
- Les accords sont maintenant ordonnés par date de signature ([#7313](https://github.com/SocialGouv/code-du-travail-numerique/issues/7313)).

### Évolutions techniques
- Mise à jour de pnpm.
- Ajout d'un système d'extraction d'événements statiques et de vérification de la dérive des événements ([#7300](https://github.com/SocialGouv/code-du-travail-numerique/issues/7300)).
- Génération de la documentation du plan de suivi à partir des événements ([#7343](https://github.com/SocialGouv/code-du-travail-numerique/issues/7343)).
- Découplage de l'affichage des accords de la recherche d'entreprise ([#7324](https://github.com/SocialGouv/code-du-travail-numerique/issues/7324)).
- Adaptation des tests E2E pour le glossaire, la recherche dans l'en-tête et les conventions collectives ([#7319](https://github.com/SocialGouv/code-du-travail-numerique/issues/7319)).

### Autres changements
- Désactivation de Husky lors d'une release.
- Mise à jour des secrets pour la preprod.
- Ajout de logs sur la recherche DILA.
