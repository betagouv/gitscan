## Changelog : pass-sport (30 derniers jours, au 09/09/2026)

### Résumé
Ce mois-ci, la plateforme a connu une évolution majeure de son interface, notamment pour le parcours "Famille Complète" qui bénéficie d'un nouveau design et de nouvelles fonctionnalités de téléchargement. Le processus d'éligibilité a été simplifié pour faciliter les démarches des utilisateurs. Parallèlement, la stabilité technique et la sécurité du service ont été renforcées par des optimisations de l'infrastructure et des processus de traitement de données en arrière-plan.

### Évolutions fonctionnelles
- **Refonte de l'expérience "Famille Complète" (FC) :** Nouvelle interface utilisateur pour le parcours FC, incluant un design modernisé des résultats et la possibilité de télécharger un document PDF ([#536](https://github.com/betagouv/pass-sport/pull/536)).
- **Simplification du parcours utilisateur :** Amélioration du test d'éligibilité et optimisation du pré-remplissage des formulaires pour les parcours hors FC ([#532](https://github.com/betagouv/pass-sport/pull/532), [#520](https://github.com/betagouv/pass-sport/pull/520)).
- **Nouveaux services de notification :** Mise en place de l'envoi d'e-mails de confirmation et d'information pour les utilisateurs ([#527](https://github.com/betagouv/pass-sport/pull/527)).
- **Amélioration de la navigation :** Ajout de raccourcis vers le code, intégration de la section "Ma demande" dans le menu et affichage des informations de contact pour le parcours FC.
- **Précisions sur les dossiers :** Ajout de détails concernant les pass enfants pour les dossiers de type "Famille Complète".
- **Clarification des contenus :** Mise à jour des libellés (wording) pour faciliter la compréhension du téléchargement du code et des différents parcours.

### Évolutions techniques
- **Optimisation de l'infrastructure Nginx :** Amélioration de la résilience (gestion des échecs d'upstream) et renforcement de la sécurité via un meilleur système de limitation de débit (*rate limiting*) basé sur l'IP réelle.
- **Optimisation des traitements de données (Batchs) :** Passage en appels asynchrones pour les processus de calcul, amélioration de la traçabilité des erreurs (stockage JSON) et ajustement de la gestion de la concurrence.
- **Amélioration de la gestion géographique :** Intégration des données INSEE en mémoire pour optimiser les recherches de localisation.
- **Renforcement de la qualité logicielle :** Ajout de configurations Playwright pour les tests d'interface et refactorisation du système d'alertes ([#526](https://github.com/betagouv/pass-sport/pull/526)).
- **Gestion des données :** Séparation des flux de données AEEH et AAH pour une meilleure précision des calculs.

### Autres changements
- **Communication :** Mise à jour des supports de communication (flyers et kit de communication).
- **Conformité et structure :** Actualisation de la politique de confidentialité, du sitemap et de la structure des pages du site.
- **Maintenance :** Nettoyage du code, mise à jour de la documentation et des notebooks de données.
