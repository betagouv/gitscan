## Changelog : transfers (30 derniers jours, au 20 août 2026)

### Résumé
Ce mois-ci, le service a franchi une étape importante avec l'introduction du chiffrement de bout en bout en option. La sécurité a été renforcée par une meilleure visibilité sur l'état des scans de fichiers et une gestion plus fine des erreurs. La gestion administrative a également été simplifiée pour faciliter le nettoyage des données obsolètes.

### Évolutions fonctionnelles
- Mise à disposition du chiffrement de bout en bout (E2EE) en option pour les transferts [#14](https://github.com/suitenumerique/transfers/issues/14).
- Possibilité pour les agents de procéder à la suppression définitive des transferts totalement désactivés [#17](https://github.com/suitenumerique/transfers/issues/17).
- Amélioration de la transparence et de la sécurité des scans : affichage systématique de l'état des scans sur les vues de transfert, gestion des timeouts et masquage des termes techniques internes dans les messages d'erreur pour éviter toute fuite d'information.

### Évolutions techniques
- Optimisation de la CI/CD : automatisation de la publication des images OCI (backend et frontend) sur GHCR et dérivation dynamique des noms de packages.
- Refactoring du backend : renommage des variables de configuration du stockage (bucket AWS) et stabilisation du processus de collecte des fichiers statiques lors de la construction.
