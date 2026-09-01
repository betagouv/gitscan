## Changelog : pass-sport (30 derniers jours, au 31/08/2026)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure avec le relancement du site. Les évolutions se sont concentrées sur l'amélioration du parcours utilisateur (éligibilité simplifiée, nouveaux systèmes d'emails, téléchargement de documents) et sur le renforcement de la robustesse technique (protection contre les bots, gestion du trafic et stabilité de l'infrastructure).

### Évolutions fonctionnelles
- Simplification du parcours d'éligibilité (test simplifié, gestion de session) [#520](https://github.com/betagouv/pass-sport/pull/520).
- Mise en place d'un système d'envoi d'emails pour les parcours "Famille Composée" (FC) et "Hors FC" [#527](https://github.com/betagouv/pass-sport/pull/527) et [#529](https://github.com/betagouv/pass-sport/pull/529).
- Amélioration de l'expérience pour les familles composées : affichage des détails du pass enfant, nouveau design des résultats et ajout du téléchargement de PDF [#531](https://github.com/betagouv/pass-sport/pull/531).
- Optimisation de l'interface et des contenus : ajustements des textes (wording), de la structure des pages, des alertes et des modèles de documents.
- Travaux en cours sur l'intégration de l'API pour les particuliers [#504](https://github.com/betagouv/pass-sport/pull/504).

### Évolutions techniques
- Sécurité et infrastructure : Ajout de règles WAF pour filtrer les bots et le trafic PHP, et correction des permissions dans les workflows CI/CD.
- Gestion du trafic : Refactorisation de la configuration du routeur et ajustement des limites de débit (rate limiting) pour stabiliser le service.
- Traitement des données : Optimisation de la génération des fichiers CSV (nommage, dates ISO, gestion des caractères spéciaux) et du stockage.
- Tests : Intégration de Playwright pour les tests d'interface utilisateur (UI).
- API : Corrections sur les appels API et le calcul du quotient familial.

### Autres changements
- Maintenance : Corrections de linting et mises à jour de sécurité des packages [#541](https://github.com/betagouv/pass-sport/pull/541) et [#547](https://github.com/betagouv/pass-sport/pull/547).
- Documentation : Mise à jour du sitemap [#540](https://github.com/betagouv/pass-sport/pull/540).
